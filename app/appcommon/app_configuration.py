# ***********************************************************************************************************#
## DATABASE CONFIGURATIONS, TABLE NAMES, COMMON DATE FORMATS

#PRESSURE POSTGRESQL DATABASE DETAILS
pressureDBConfig = {
    "host": "192.168.0.101",
    "user": "postgres",
    "password": "1234",
    "database": "pressure",
    "port":"5002",
}
#HUMIDITY POSTGRESQL DATABASE DETAILS
humidityDBConfig = {
    "host": "192.168.0.101",
    "user": "postgres",
    "password": "1234",
    "database": "humidity",
    "port":"5004",
}
#TEMPERATURE POSTGRESQL DATABASE DETAILS
temperatureDBConfig = {
    "host": "192.168.0.101",
    "user": "postgres",
    "password": "1234",
    "database": "temperature",
    "port":"5003",
}

#PRESSURE TABLE NAME USED IN DATABASE
pressureTableName = "pressuretable"
temperatureTableName = "temperaturetable"
humidityTableName = "humiditytable"

#DATE FORMAT USED IN PRESSURE TABLE
pressureTableDateFormat = '%Y-%m-%d %H:%M:%S'
temperatureTableDateFormat = '%Y-%m-%d %H:%M:%S'
humidityTableDateFormat = '%Y-%m-%d %H:%M:%S'
dateFormat = '%Y-%m-%d %H:%M:%S'

# ***********************************************************************************************************#

#PORT NUMBER DETAILS
portForLiveDataFetching = 4001          #For running Live Data micro service
portForPressureData = 4002              #For running Pressure micro services
portForTemperatureData = 4003           #For running Temperature micro service
portForHumidityData = 4004              #For running Humidity micro service


#HOST NAME DETAILS
hostNameForLiveDataFetching = "0.0.0.0"
hostNameForPressureData = "0.0.0.0"
hostNameForTemperatureData = "0.0.0.0"
hostNameForHumidityData = "0.0.0.0"