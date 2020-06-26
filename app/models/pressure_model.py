import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
import json
from datetime import datetime, timedelta
import os, sys
sys.path.append(os.getcwd())
import app.appcommon.app_configuration as appConf    #Input File for providing DB details, table name, common string formats
import app.appcommon.app_constants as constant  #Importing Constant variables file

class staticVar:
    connection = ""
    isDBConnected = False
    cursor = ""
    DBConnectionData = {"statusCode":None,"connectionMsg":None} ##Database Connection Codes and Messages >>> Success:0, FAILED:1
    DBQueryStatus = {"statusCode":None,"queryResult":None,"statusMessage":None} ##Database Query Codes and Messages >>> Success:0, FAILED:1
    dataFrom = ""
    dataTill = ""
    days_to_subtract = 0
    

def getDbConnection():
    try:
        #DB Details fetched from the Configuration file
        staticVar.connection = psycopg2.connect(user = appConf.pressureDBConfig["user"],
                                        password = appConf.pressureDBConfig["password"],
                                        host = appConf.pressureDBConfig["host"],
                                        port = appConf.pressureDBConfig["port"],
                                        database = appConf.pressureDBConfig["database"])
        staticVar.cursor = staticVar.connection.cursor()
        staticVar.isDBConnected = True
        staticVar.DBConnectionData["statusCode"] = constant.SUCESS_STATUS_CODE
        staticVar.DBConnectionData["connectionMsg"] = constant.SUCESS_STATUS_MESSAGE
        return staticVar.DBConnectionData
    except (Exception, psycopg2.Error) as error :
        staticVar.DBConnectionData["statusCode"] = constant.FAILED_STATUS_CODE
        staticVar.DBConnectionData["connectionMsg"] = constant.FAILED_STATUS_MESSAGE
        return staticVar.DBConnectionData

def dbConnector():
    if (staticVar.isDBConnected):
        print("Db Already connected",staticVar.isDBConnected)
        return
    else:
        print("Creating new DB Connection")
        getDbConnection()

def isTableExist(tableName):
    try:
        dbConnector()
        table_exist_query = "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name ='"+tableName+"');"
        staticVar.cursor.execute(table_exist_query) # Should be logged
        if(staticVar.cursor.fetchone()[0]):
            return True
        else:
            return False
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while checking whether "+tableName+" Table is present or not>>", error) # Should be logged
        return ("Error while checking whether "+tableName+" Table is present or not>>", error)

def dropTable(tableName):
    try:
        if(isTableExist(tableName)):
            dbConnector()
            staticVar.cursor.execute("DROP TABLE "+tableName+" CASCADE;")
            staticVar.connection.commit()
            queryStatusUpdate(constant.SUCESS_STATUS_CODE,constant.SUCESS_STATUS_MESSAGE,constant.POSTGRESQL_DB_DROP_TABLE_SUCCESS_MESSAGE)
        else:
            queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,constant.POSTGRESQL_DB_TABLE_NOT_EXIST_MESSAGE)
        
        return {"TableName":tableName,"queryStatusUpdate": staticVar.DBQueryStatus}
    except (Exception, psycopg2.DatabaseError) as error :
        queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,f"{constant.POSTGRESQL_DB_DROP_TABLE_FAILURE_MESSAGE} >>> {error}")
        return {"TableName":tableName,"queryStatusUpdate": staticVar.DBQueryStatus}
    
def createPressureTable():
    try:        
        if (isTableExist(appConf.pressureTableName)):
            return(constant.TABLE_EXIST_MESSAGE)
        else:
            dbConnector()
            create_table_query = f'CREATE TABLE IF NOT EXISTS public."{appConf.pressureTableName}"(fetchedTime TIMESTAMP NOT NULL, fetchedData jsonb NOT NULL, PRIMARY KEY (fetchedTime));'
            alter_table_query = f'ALTER TABLE public."{appConf.pressureTableName}" OWNER to {appConf.pressureDBConfig["user"]};'
            # print(create_table_query)
            # print(alter_table_query)
            staticVar.cursor.execute(create_table_query)
            staticVar.cursor.execute(create_table_query)
            staticVar.connection.commit()
            return constant.POSTGRESQL_DB_CREATE_TABLE_SUCCESS_MESSAGE # Should be logged

    except (Exception, psycopg2.DatabaseError) as error :
        queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,f"{constant.POSTGRESQL_DB_INSERTION_FAILURE_MESSAGE} >>> {error}")
        print ("Error while creating PostgreSQL table", error) # Should be logged
        return ("Error while creating PostgreSQL table", error)

def insertDataIntoTable(tableName,fetchedtime,fetcheddata):
    try:
        dbConnector()
        # print("inside insertdata")
        # if (isTableExist(tableName) == False):
        #     createPressureTable()
        # print(tableName,fetchedtime,fetcheddata)
        # insert_query = 'INSERT INTO public.%s VALUES(%s,%s);'
        # insert_query = f'INSERT INTO {tableName} VALUES ({fetchedTime},{fetcheddata});'
        insert_query = "INSERT INTO "+tableName+" VALUES ('"+fetchedtime+"', '"+fetcheddata+"'::jsonb );"
        print(insert_query)
        record_to_insert = (tableName,fetchedtime,fetcheddata)
        print(insert_query)
        staticVar.cursor.execute(insert_query)
        staticVar.connection.commit()
        print("done inserting")
        count = staticVar.cursor.rowcount
        queryStatusUpdate(constant.SUCESS_STATUS_CODE,constant.SUCESS_STATUS_MESSAGE,f"{count} {constant.POSTGRESQL_DB_INSERTION_SUCESS_MESSAGE}")
        
        return staticVar.DBQueryStatus      # Should be logged
    except (Exception, psycopg2.DatabaseError) as error :
        queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,f"{constant.POSTGRESQL_DB_INSERTION_FAILURE_MESSAGE} >>> {error}")
        return staticVar.DBQueryStatus # Should be logged

def fetchDataFromTable(tableName,timeperiod):
    try:
        dbConnector()
        if (isTableExist(tableName) == False):
            createPressureTable()
        staticVar.cursor =  staticVar.connection.cursor(cursor_factory=RealDictCursor)
        if(timeperiod.lower()=='lastweek'):
            staticVar.days_to_subtract = 7
        elif(timeperiod.lower()=='last24hours'):
            staticVar.days_to_subtract = 1
        currenttime = datetime.now()
        currenttime = currenttime.strftime(appConf.dateFormat)
        currenttime = datetime.strptime(currenttime, appConf.dateFormat)
        staticVar.dataFrom = currenttime - timedelta(days=staticVar.days_to_subtract)
        staticVar.dataTill = currenttime
        staticVar.dataFrom = staticVar.dataFrom.strftime(appConf.dateFormat)
        staticVar.dataTill =  staticVar.dataTill.strftime(appConf.dateFormat)

        fetch_query = "SELECT fetcheddata FROM "+tableName+" WHERE FetchedTime >='"+ staticVar.dataFrom+"' AND FetchedTime < '"+ staticVar.dataTill+"' order by fetchedTime asc;"
        print("*********",fetch_query) # Should be logged
        staticVar.cursor.execute(fetch_query)
        staticVar.connection.commit()
        allPressureData = staticVar.cursor.fetchall()
        results = {}
        count = 0
        for row in allPressureData:
            results[count] = row
            count = count + 1

        queryStatusUpdate(constant.SUCESS_STATUS_CODE,constant.SUCESS_STATUS_MESSAGE, constant.POSTGRESQL_DB_DATA_FETCHING_SUCCESS_MESSAGE)
        return results
    except (Exception, psycopg2.DatabaseError) as error :
        queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE, constant.POSTGRESQL_DB_DATA_FETCHING_FAILED_MESSAGE)
        print ("Error while fetching data from PostgreSQL table", error,">>> ",staticVar.DBQueryStatus)    # Should be logged     
        return staticVar.DBQueryStatus

def queryStatusUpdate(statusCode,queryResult,statusMessage):
    staticVar.DBQueryStatus["statusCode"] = statusCode
    staticVar.DBQueryStatus["queryResult"] = queryResult
    staticVar.DBQueryStatus["statusMessage"] = statusMessage
     # Should be logged

def closeConnection():
    try:
        if(staticVar.isDBConnected):
            staticVar.cursor.close()
            staticVar.connection.close()
            staticVar.isDBConnected = False
            print(f"{constant.POSTGRESQL_DB_CLOSE_CONNECTION_SUCCESS_MESSAGE} >>> DB Connection Status >>> {staticVar.isDBConnected}")
            return constant.POSTGRESQL_DB_CLOSE_CONNECTION_SUCCESS_MESSAGE # Should be logged
    except (Exception, psycopg2.Error) as error :
        print (f"{constant.POSTGRESQL_DB_CLOSE_CONNECTION_FAILURE_MESSAGE} >>> {error}") # Should be logged
        return (f"{constant.POSTGRESQL_DB_CLOSE_CONNECTION_FAILURE_MESSAGE} >>> {error}") # Should be logged
