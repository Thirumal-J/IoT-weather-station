import os
from flask import Flask , jsonify , request
from flask_restful import Resource, Api
import sqlite3
import socket
import json
import os, sys
sys.path.append(os.getcwd())
import app.appcommon.app_configuration as appConf
import app.models.temperature_model as temperatureModel

app = Flask(__name__)
api = Api(app)

class TestConnection(Resource):
    def get(self):
        return "Connection Successful"
    
    def post(self):
        inputJson = request.get_json()
        return {"input data":inputJson},201

class DBConnection(Resource):
    def get(self):
        return temperatureModel.getDbConnection()

class FetchAllTemperatureData(Resource):
    def get(self,timeperiod):
        print(timeperiod)
        tempdata = temperatureModel.fetchDataFromTable(appConf.temperatureTableName,timeperiod)
        return jsonify(tempdata)

class DropTemperatureTable(Resource):
    def delete(self, tableName):
        status=temperatureModel.dropTable(appConf.temperatureTableName)
        return {"status":status}

class CreateTemperatureTable(Resource):
    def get(self):
        status = temperatureModel.createTemperatureTable()
        return {"status":status}

class InsertTemperatureData(Resource):
    def post(self):
        inputJson = request.get_json()
        return temperatureModel.insertDataToTable(appConf.temperatureTableName,inputJson["fetchedUnit"],inputJson["fetchedValue"],inputJson["fetchedTime"])

api.add_resource(TestConnection,"/")
api.add_resource(DBConnection,"/getDbConnection")
api.add_resource(FetchAllTemperatureData,"/temperatureData/<timeperiod>")
api.add_resource(DropTemperatureTable,"/dropTableTemperature/<tableName>")
api.add_resource(InsertTemperatureData,"/insertTemperatureData")
api.add_resource(CreateTemperatureTable,"/createTemperatureTable")

if __name__ == "__main__":
    TemperatureDbConnection = temperatureModel.getDbConnection()
    print(TemperatureDbConnection)
    if (TemperatureDbConnection["statusCode"]==0):
        app.run(host=appConf.hostNameForTemperatureData, port=appConf.portForTemperatureData)
        temperatureModel.closeConnection()