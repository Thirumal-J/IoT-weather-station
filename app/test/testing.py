import PressureDatabaseDAO as pressureDBDao
import psycopg2
from psycopg2 import Error
import Configuration as conf
from datetime import datetime, timedelta
import SensorHandler as sensorHandler
import json
import sqlite3


# import LiveDataMicroService as liveDataDao

class staticVar:
    global dataFrom, dataTill
    data = []
# pressureDBDao.dropTable(pressureTableName)
# pressureDBDao.createPressureTable()

# pressureDBDao.fetchDataFromTable(pressureTableName)
sensedValues = sensorHandler.getAllValuesFromSensor()
print("sensedValues >>>",sensedValues)
pressureData = sensedValues.get("pressure")
pressureData["createdTime"]= sensedValues.get("createdTime")
createdDateTimeAsObj = datetime.strptime(sensedValues.get("createdTime"), conf.pressureTableDateFormat)

print("pressureData >>>",pressureData["value"])

# liveDataDao.updateLiveData(sensedValues)
# insert_query = "INSERT INTO "+conf.pressureTableName+" VALUES ('"+createdDateTimeAsObj+"', '"+json.dumps(pressureData)+"'::jsonb );"
# print("INSERT_QUERY IN TESTING FILE>>>",insert_query)
# pressureDBDao.insertDataIntoTable(conf.pressureTableName, createdDateTimeAsObj, json.dumps(pressureData))
# results =  pressureDBDao.fetchDataFromTable(conf.pressureTableName,"last24hours")
# print(results)
# print(">>>OUTPUT LIVEDATA>>>",liveDataDao.getLiveData())


# staticVar.data.append(sensedValues)
# with open('SensedDataJson.txt', 'w') as outfile:
#     json.dump(staticVar.data, outfile)


# pressureDBDao.closeConnection()