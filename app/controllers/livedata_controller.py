from flask import Flask, request
from flask_restful import Resource, Api
import socket
import json
import os, sys
sys.path.append(os.getcwd())
import app.models.livedata_model as livedataModel
import app.appcommon.app_configuration as appConf


app = Flask(__name__)
api = Api(app)

class FetchLiveData(Resource):
    def get(self):
        return  livedataModel.getLiveData()   #Providing the last fetched data

api.add_resource(FetchLiveData,"/fetchLiveWeather")

if __name__ == '__main__':
    app.run(host=appConf.hostNameForLiveDataFetching,port=appConf.portForLiveDataFetching,debug=False)

