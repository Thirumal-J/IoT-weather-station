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
        print(timeperiod) # Should be logged
        sensedPressureValues = pressureModel.fetchDataFromTable(appConf.pressureTableName,timeperiod)
        return sensedPressureValues

class DropTable(Resource):
    def delete(self, tableName):
        status = pressureModel.dropTable(appConf.pressureTableName)# for pressure table
        return {"Status":status}

class CreatePressureTable(Resource):
    def get(self):
        status = pressureModel.createPressureTable()
        return {"Status":status}

class InsertPressureData(Resource):
    def post(self):
        inputJson = request.get_json()
        return pressureModel.insertDataIntoTable(appConf.pressureTableName,inputJson["fetchedTime"],inputJson["fetchedData"])

api.add_resource(DBConnection,"/getDbConnection")
api.add_resource(FetchAllPressureData,"/pressureData/<timeperiod>")
api.add_resource(DropTable,"/dropTable/<tableName>")#Only for testing
api.add_resource(CreatePressureTable,"/createPressureTable")#Only for testing
api.add_resource(InsertPressureData,"/insertPressureData")#Only for testing

if __name__ == '__main__':
    PressureDbConnection = pressureModel.getDbConnection()
    print(PressureDbConnection)
    if (PressureDbConnection["statusCode"]==0):
        app.run(host=appConf.hostNameForPressureData,port=appConf.portForPressureData,debug=False)
        pressureModel.closeConnection()