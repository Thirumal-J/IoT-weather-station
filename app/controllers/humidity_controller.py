from flask import Flask , jsonify , request
from flask_restful import Resource, Api
import sqlite3
import socket
import json
import os, sys
sys.path.append(os.getcwd())
import app.models.humidity_model as humidityModel
import app.appcommon.app_configuration  as appConf

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
        return humidityModel.getDbConnection()

class FetchAllHumidityData(Resource):
    def get(self,timeperiod):
        print(timeperiod)
        humiditydata = humidityModel.fetchDataFromTable(appConf.humidityTableName,timeperiod)
        return jsonify(humiditydata)

class DropHumidityTable(Resource):
    def delete(self, tableName):
        status=humidityModel.dropTable(appConf.humidityTableName)
        return {"status":status}

class CreateHumidityTable(Resource):
    def get(self):
        status = humidityModel.CreateHumidityTable()
        return {"status":status}

class InsertHumidityData(Resource):
    def post(self):
        inputJson = request.get_json()
        return humidityModel.insertDataToTable(appConf.humidityTableName,inputJson["fetchedUnit"],inputJson["fetchedValue"],inputJson["fetchedTime"])

api.add_resource(TestConnection,"/")
api.add_resource(DBConnection,"/getDbConnection")
api.add_resource(FetchAllHumidityData,"/humidityData/<timeperiod>")
api.add_resource(DropHumidityTable,"/dropHumidityTable/<tableName>")
api.add_resource(InsertHumidityData,"/insertHumidityData")
api.add_resource(CreateHumidityTable,"/createHumidityTable")

if __name__ == "__main__":
#  app.run(debug=False)
   #app.run(host='0.0.0.0' , port = 4000, debug=False)
   HumidityDbConnection = humidityModel.getDbConnection()
   print(HumidityDbConnection)
   if (HumidityDbConnection["statusCode"]==0):
       app.run(host=appConf.hostNameForHumidityData, port=appConf.portForHumidityData,debug=False)
       humidityModel.closeConnection()
