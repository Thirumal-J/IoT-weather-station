import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
# from SensorHandler import *
import json
import time
from datetime import datetime, timedelta
import os, sys
sys.path.append(os.getcwd())
import app.models.temperature_model as temperatureModel
import app.appcommon.app_configuration as appConf    #Input File for providing DB details, table name, common string formats

global initialValues, sensedValues

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/senseHat/fetchTemperatureData",qos=1)

def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")

def on_message(client, userdata, msg):
    temperatureData = json.loads(msg.payload.decode("utf-8"))
    print("temperatureData >>>",temperatureData)

    createdDateTimeAsObj = datetime.strptime(temperatureData.get("createdTime"), appConf.dateFormat)
    createdDateTimeAsObj = createdDateTimeAsObj.strftime(appConf.dateFormat)
    temperatureModel.insertDataToTable(appConf.temperatureTableName,temperatureData["unit"],temperatureData["value"],createdDateTimeAsObj)
      
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_forever()