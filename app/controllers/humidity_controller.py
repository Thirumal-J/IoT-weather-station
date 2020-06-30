from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2
import socket
import json
import os, sys
sys.path.append(os.getcwd())
import app.models.humidity_model as humidityModel
import app.appcommon.app_configuration as appConf

app = Flask(__name__)
api = Api(app)

class DBConnection(Resource):
    def get(self):
        return humidityModel.getDbConnection()

# MAIN MICRO SERVCICE FOR PRESSURE
class FetchAllHumidityData(Resource):
    def get(self,timeperiod):
        print(timeperiod) # Should be logged
        sensedHumidityValues = humidityModel.fetchDataFromTable(appConf.humidityTableName,timeperiod)
        return sensedHumidityValues

class DropTable(Resource):
    def delete(self):
        status = humidityModel.dropTable(appConf.humidityTableName)# for humidity table
        return {"Status":status}

class CreateHumidityTable(Resource):
    def get(self):
        status = humidityModel.createHumidityTable()
        return {"Status":status}

class InsertHumidityData(Resource):
    def post(self):
        inputJson = request.get_json()
        status = humidityModel.insertDataIntoTable(appConf.humidityTableName,inputJson["fetchedTime"],inputJson["fetchedData"])
        return {"Status":status} 

api.add_resource(DBConnection,"/getDbConnection")
api.add_resource(FetchAllHumidityData,"/humidityData/<timeperiod>")
api.add_resource(DropTable,"/dropTable")#Only for testing
api.add_resource(CreateHumidityTable,"/createHumidityTable")#Only for testing
api.add_resource(InsertHumidityData,"/insertHumidityData")#Only for testing

if __name__ == '__main__':
    app.run(host=appConf.hostNameForHumidityData,port=appConf.portForHumidityData,debug=False)