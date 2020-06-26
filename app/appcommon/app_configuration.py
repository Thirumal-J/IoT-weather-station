# ***********************************************************************************************************#
## DATABASE CONFIGURATIONS, TABLE NAMES, COMMON DATE FORMATS

#PRESSURE DATABASE DETAILS
pressureDBConfig = {
    "host": "127.0.0.1",
    "user": "postgres",
    "password": "miciotproject",
    "database": "pressuredb",
    "port":"5432",
}
#TEMPERATURE DATABASE DETAILS
temperatureDBConfig = {
	"database": "temperaturedb"
}

#HUMIDITY DATABASE DETAILS
humidityDBConfig = {
	"database": "humiditydb"
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