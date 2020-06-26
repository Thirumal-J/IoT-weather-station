import sqlite3 as lite
from sqlite3 import Error
from datetime import datetime, timedelta
import os, sys
sys.path.append(os.getcwd())
import app.appcommon.app_configuration as appConf
import app.appcommon.app_constants as constant

class con: 
   connection = ""
   cursor = ""
   isDBConnected = False
   DBConnectionData = {"statusCode":None,"connectionMsg":None}
   DBQueryStatus = {"statusCode":None,"queryResult":None,"statusMessage":None}
   dataFrom = ""
   dataTill = ""
   days_to_subtract = 0

staticObj = con()
def getDbConnection():
    try:
        con.connection  = lite.connect("humiditydb.db", check_same_thread=False)
        con.cursor= con.connection.cursor()
        con.isDBConnected = True
        con.DBConnectionData["statusCode"] = 0
        con.DBConnectionData["connectionMsg"] = "SUCCESS"
        return con.DBConnectionData
    except (Exception, lite.DatabaseError) as error:
        con.DBConnectionData["statusCode"] = 1
        con.DBConnectionData["connectionMsg"] = f"ERROR :{error}"
        return con.DBConnectionData

def dbConnector():
    if(con.isDBConnected):
        print("Already dbConnected >>>   ")
        return
    else:
        print("Creating new dbConnection >>>   ")
        getDbConnection()

def isTableExist(tableName):
    try:
        dbConnector()
        table_exist_query = "SELECT EXISTS(SELECT NAME FROM sqlite_master WHERE type='table' and name='"+tableName+"');"
        con.cursor.execute(table_exist_query)
        if(con.cursor.fetchone()[0]):
            return True
        else:
            return False
    except (Exception, lite.DatabaseError) as error :
        print ("Error while checking whether "+tableName+" Table is present or not>>", error)
        return ("Error while checking whether "+tableName+" Table is present or not>>", error)

def dropTable(tableName):
    try:
        if(isTableExist(tableName)):
            dbConnector()
            con.cursor.execute("DROP TABLE "+tableName+";")
            con.connection.commit()
        else:
           queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,constant.SQLITE3_TABLE_NOT_EXIST_MESSAGE)
           return {"TableName":tableName,"queryStatusUpdate": con.DBQueryStatus}

    except (Exception, lite.DatabaseError) as error :
       queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,f"{constant.SQLITE3_DROP_TABLE_FAILURE_MESSAGE} >>> {error}")
       return {"TableName":tableName,"queryStatusUpdate": con.DBQueryStatus}
    
def CreateHumidityTable(tableName):
    try:        
        if (isTableExist(tableName)):
            return("Table is already exist")
        else:
            dbConnector()
            create_table_query = "CREATE TABLE "+tableName+"(fetchedUnit VARCHAR, fetchedValue NUMERIC, fetchedTime TIMESTAMP NOT NULL, PRIMARY KEY (fetchedTime));"
            #alter_table_query = 'ALTER TABLE public."{humidityTableName}" OWNER to postgres;'
            print(create_table_query)
            #print(alter_table_query)
            con.cursor.execute(create_table_query)
            con.connection.commit()
            print(isTableExist(tableName))
            return ("Table created successfully in sqlite ")

    except (Exception, lite.DatabaseError) as error :
        queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,f"{constant.SQLITE3_INSERTION_FAILURE_MESSAGE} >>> {error}")
        print ("Error while creating sqlite table", error)
        return ("Error while creating sqlite table", error)

def insertDataToTable(tableName,fetchedunit,fetchedvalue,fetchedtime):
    try:
        dbConnector()
        con.connection.row_factory = dict_factory
        #insert_query = "INSERT INTO %s VALUES(%s,%s);" 
        insert_query = "INSERT INTO "+tableName+"(fetchedUnit,fetchedValue,fetchedTime) VALUES(?, ?, ?);"
        data_tuple = (fetchedunit,fetchedvalue,fetchedtime)
        #record_to_insert = (tableName,fetchedUnit,fetchedValue,fetchedTime)
        print(insert_query)

        #con.cursor.execute(insert_query,record_to_insert)
        con.cursor.execute(insert_query, data_tuple)
        # con.cursor.execute(insert_query)
        con.connection.commit()
        print("done inserting")
        count = con.cursor.rowcount
        queryStatusUpdate(constant.SUCESS_STATUS_CODE,constant.SUCESS_STATUS_MESSAGE,f"{count} {constant.SQLITE3_INSERTION_SUCESS_MESSAGE}")
        return con.DBQueryStatus       
    except (Exception, lite.DatabaseError) as error :
        queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE,f"{constant.SQLITE3_INSERTION_FAILURE_MESSAGE} >>> {error}")
        return con.DBQueryStatus

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def fetchDataFromTable(tableName,timeperiod):
    try:
        dbConnector()
        #con.cursor.row_factory = dict_factory
        if(timeperiod.lower()=='lastweek'):
            con.days_to_subtract = 7
        elif(timeperiod.lower()=='last24hours'):
            con.days_to_subtract = 1
        currenttime = datetime.now()
        currenttime = currenttime.strftime(appConf.dateFormat)
        currenttime = datetime.strptime(currenttime, appConf.dateFormat)
        con.dataFrom = currenttime - timedelta(days=con.days_to_subtract)
        con.dataTill = currenttime
        con.dataFrom = con.dataFrom.strftime(appConf.dateFormat)
        con.dataTill =  con.dataTill.strftime(appConf.dateFormat)
       
        fetch_query = "SELECT * FROM "+tableName+" WHERE "+tableName+".FetchedTime >= '"+con.dataFrom+"' AND "+tableName+".FetchedTime < '"+con.dataTill+"' order by fetchedtime asc;"
        print("*********",fetch_query)   
        con.cursor.execute(fetch_query)
        con.connection.commit()
        allhumidityData = con.cursor.fetchall()
        results = {}
        count = 0
        for row in allhumidityData:
            results[count] = { 'fetcheddata':{'unit': row[0], 'value': row[1] ,'createdtime': row[2]}}
            count = count + 1
        queryStatusUpdate(constant.SUCESS_STATUS_CODE,constant.SUCESS_STATUS_MESSAGE, constant.SQLITE3_DATA_FETCHING_SUCCESS_MESSAGE)      
        return results
        
    except (Exception, lite.DatabaseError) as error :
        queryStatusUpdate(constant.FAILED_STATUS_CODE,constant.FAILED_STATUS_MESSAGE, constant.SQLITE3_DATA_FETCHING_FAILED_MESSAGE)
        print ("Error while fetching data from sqlite table", error)     
        return con.DBQueryStatus

def queryStatusUpdate(statusCode,queryResult,statusMessage):
    con.DBQueryStatus["statusCode"] = statusCode
    con.DBQueryStatus["queryResult"] = queryResult
    con.DBQueryStatus["statusMessage"] = statusMessage


def closeConnection():
    try:
        if(con.isDBConnected):
            con.cursor.close()
            con.connection.close()
            con.isDBConnected = False
            print(f"{constant.SQLITE3_CLOSE_CONNECTION_SUCCESS_MESSAGE} >>> DB Connection Status >>> {con.isDBConnected}")
            return constant.SQLITE3_CLOSE_CONNECTION_SUCCESS_MESSAGE # Should be logged
    except (Exception, lite.DatabaseError) as error :
        print (f"{constant.SQLITE3_CLOSE_CONNECTION_FAILURE_MESSAGE} >>> {error}") # Should be logged
        return (f"{constant.SQLITE3_CLOSE_CONNECTION_FAILURE_MESSAGE} >>> {error}") # Should be logged