import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
# from SensorHandler import *
import json
import time
from datetime import datetime, timedelta
import os, sys
sys.path.append(os.getcwd())
import app.models.livedata_model as livedataModel

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/senseHat/fetchLiveData",qos=1)

def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")

def on_message(client, userdata, msg):
    liveData = json.loads(msg.payload.decode("utf-8"))
    print("liveData >>>",liveData)
    livedataModel.updateSensedDataAsJson(liveData)

      
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect


client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_forever()