import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
# from SensorHandler import *
import json
import time
from datetime import datetime, timedelta
import os, sys
sys.path.append(os.getcwd())
import app.models.humidity_model as humidityModel
import app.appcommon.app_configuration as appConf

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/senseHat/fetchHumidityData")

def on_message(client, userdata, msg):
    humidityData = json.loads(msg.payload.decode("utf-8"))
    print("humidityData >>>",humidityData)

    createdDateTimeAsObj = datetime.strptime(humidityData.get("createdTime"), appConf.dateFormat)
    createdDateTimeAsObj = createdDateTimeAsObj.strftime(appConf.dateFormat)
    humidityModel.insertDataToTable(appConf.humidityTableName,humidityData["unit"],humidityData["value"],createdDateTimeAsObj)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_forever()