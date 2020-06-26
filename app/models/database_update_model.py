import json
from datetime import datetime, timedelta
import time
import os, sys
sys.path.append(os.getcwd())
import app.appcommon.app_configuration as appConf
import app.models.livedata_model as livedataModel
import app.models.pressure_model as pressureModel
import app.models.humidity_model as humidityModel
import app.models.temperature_model as temperatureModel
import pymsgbox

def updateAllDatabase(sensedValues):

    #FOR LIVE DATA UPDATE
    livedataModel.updateSensedDataAsJson(sensedValues)
    pymsgbox.alert("Completed Json file update")

    createdDateTimeAsObj = datetime.strptime(sensedValues.get("createdTime"), appConf.pressureTableDateFormat)
    createdDateTimeAsObj = createdDateTimeAsObj.strftime(appConf.pressureTableDateFormat)

    #FOR PRESSURE DATABASE INSERTION
    pymsgbox.alert("PRESSURE DB INSERTION")
    pressureData = sensedValues.get("pressure")
    pressureData["createdTime"]= sensedValues.get("createdTime")
    pressureModel.insertDataIntoTable(appConf.pressureTableName, createdDateTimeAsObj, json.dumps(pressureData))
    pymsgbox.alert("PRESSURE DB INSERTION COMPLETED")
    #FOR TEMPERATURE DATABASE INSERTION
    temperatureModel.insertDataToTable(appConf.temperatureTableName,sensedValues["temperature"]["unit"],sensedValues["temperature"]["value"],createdDateTimeAsObj)    

    #FOR HUMIDITY DATABASE INSERTION
    pymsgbox.alert("HUMIDITY DB INSERTION")
    humidityModel.insertDataToTable(appConf.humidityTableName,sensedValues["humidity"]["unit"],sensedValues["humidity"]["value"],createdDateTimeAsObj)
    pymsgbox.alert("HUMIDITY DB INSERTION COMPLETED")