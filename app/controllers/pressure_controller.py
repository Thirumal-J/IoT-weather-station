from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2
import socket
import json
import os, sys
sys.path.append(os.getcwd())
import app.models.pressure_model as pressureModel
import app.appcommon.app_configuration as appConf

app = Flask(__name__)
api = Api(app)

class DBConnection(Resource):
    def get(self):
        return pressureModel.getDbConnection()

# MAIN MICRO SERVCICE FOR PRESSURE
class FetchAllPressureData(Resource):
    def get(self,timeperiod):
        sensedPressureValues = pressureModel.fetchDataFromTable(appConf.pressureTableName,timeperiod)
        return sensedPressureValues

class DropTable(Resource):
    def delete(self):
        status = pressureModel.dropTable(appConf.pressureTableName)# for pressure table
        return {"status":status}

class CreatePressureTable(Resource):
    def get(self):
        status = pressureModel.createPressureTable()
        return {"status":status}

class InsertPressureData(Resource):
    def post(self):
        inputJson = request.get_json()
        status = pressureModel.insertDataIntoTable(appConf.pressureTableName,inputJson["fetchedTime"],inputJson["fetchedData"])
        return {"status":status} 

api.add_resource(DBConnection,"/getDbConnection")
api.add_resource(FetchAllPressureData,"/pressureData/<timeperiod>")
api.add_resource(DropTable,"/dropTable")#Only for testing
api.add_resource(CreatePressureTable,"/createPressureTable")#Only for testing
api.add_resource(InsertPressureData,"/insertPressureData")#Only for testing

if __name__ == '__main__':
    app.run(host=appConf.hostNameForPressureData,port=appConf.portForPressureData,debug=False)