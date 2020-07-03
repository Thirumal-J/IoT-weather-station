from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2
import socket
import json
import os, sys
sys.path.append(os.getcwd())
import app.models.temperature_model as temperatureModel
import app.appcommon.app_configuration as appConf

app = Flask(__name__)
api = Api(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

    
class DBConnection(Resource):
    def get(self):
        return temperatureModel.getDbConnection()

# MAIN MICRO SERVCICE FOR PRESSURE
class FetchAllTemperatureData(Resource):
    def get(self,timeperiod):
        print(timeperiod) # Should be logged
        sensedTemperatureValues = temperatureModel.fetchDataFromTable(appConf.temperatureTableName,timeperiod)
        return sensedTemperatureValues

class DropTable(Resource):
    def delete(self):
        status = temperatureModel.dropTable(appConf.temperatureTableName)# for temperature table
        return {"status":status}

class CreateTemperatureTable(Resource):
    def get(self):
        status = temperatureModel.createTemperatureTable()
        return {"status":status}

class InsertTemperatureData(Resource):
    def post(self):
        inputJson = request.get_json()
        status = temperatureModel.insertDataIntoTable(appConf.temperatureTableName,inputJson["fetchedTime"],inputJson["fetchedData"])
        return {"status":status} 

api.add_resource(DBConnection,"/getDbConnection")
api.add_resource(FetchAllTemperatureData,"/temperatureData/<timeperiod>")
api.add_resource(DropTable,"/dropTable")#Only for testing
api.add_resource(CreateTemperatureTable,"/createTemperatureTable")#Only for testing
api.add_resource(InsertTemperatureData,"/insertTemperatureData")#Only for testing

if __name__ == '__main__':
    app.run(host=appConf.hostNameForTemperatureData,port=appConf.portForTemperatureData,debug=False)