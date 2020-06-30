#!/bin/bash
python ./app/controllers/humidity_controller.py &
python ./app/controllers/temperature_controller.py &
python ./app/controllers/pressure_controller.py &
python ./app/controllers/livedata_controller.py &
python ./app/mqtt/mqtt_client_handler.py &
python ./app/mqtt/live_data_mqtt.py &
python ./app/mqtt/pressure_mqtt.py &
python ./app/mqtt/temperature_mqtt.py &
python ./app/mqtt/humidity_mqtt.py 
