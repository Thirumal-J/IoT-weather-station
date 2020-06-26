# from sense_hat import SenseHat
import datetime
import sys
import random

def getAllValuesFromSensor():
    # sense = SenseHat()
    # sense.clear()
    
    # temp = sense.get_temperature()
    temp = random.randint(1,110)
    temperature = str(round(temp,1))

    # humidity = sense.get_humidity()
    humidity = random.randint(1,100)
    humidity = str(round(humidity, 1))

    # pressure = sense.get_pressure()		
    pressure = random.randint(700,1200)	
    pressure = str(round(pressure, 1))
    
    #timeValue = time.asctime(time.localtime(time.time()))
    timeValue = datetime.datetime.now()
    timeValue = timeValue.strftime("%Y-%m-%d %H:%M:%S")

    sensedValues = {"temperature":{"value":temperature, "unit":"celsius"},"pressure":{"value":pressure, "unit":"hpa"},"humidity":{"value":humidity,"unit":"%"},"createdTime":timeValue}
    #sense.show_message("Temp in C--->" + str(tempInCelsius) +  "   Humidity-->" + str(humidity) + " Pressure-->" + str(pressure), scroll_speed=(0.08), back_colour= [0,0,0])
    return sensedValues


