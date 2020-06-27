import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
# from SensorHandler import *
import json
import time
from datetime import datetime, timedelta
import os, sys
sys.path.append(os.getcwd())

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/senseHat/fetchWeatherReport",qos=1)
    print("Done")

def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("INSIDE MESSAGE>>>",msg)
    sensedValues = json.loads(msg.payload.decode("utf-8"))
    print("sensedValues >>>",sensedValues)
    publish.single("/senseHat/fetchLiveData",json.dumps(sensedValues), hostname="mqtt.eclipse.org",qos=1)

    pressureData = sensedValues.get("pressure")
    pressureData["createdTime"]= sensedValues.get("createdTime")
    publish.single("/senseHat/fetchPressureData",json.dumps(pressureData), hostname="mqtt.eclipse.org",qos=1)

    humidityData = sensedValues.get("humidity")
    humidityData["createdTime"]= sensedValues.get("createdTime")
    publish.single("/senseHat/fetchHumidityData",json.dumps(humidityData), hostname="mqtt.eclipse.org",qos=1)

    temperatureData = sensedValues.get("temperature")
    temperatureData["createdTime"]= sensedValues.get("createdTime")
    publish.single("/senseHat/fetchTemperatureData",json.dumps(temperatureData), hostname="mqtt.eclipse.org",qos=1)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect


client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()