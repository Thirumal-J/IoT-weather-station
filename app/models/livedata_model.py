import json
import os, sys
import glob
sys.path.append(os.getcwd())
from pathlib import Path

class staticVariable:
        liveData = []
        sensed_data_json_file = ""
        # For accessing the file inside a sibling folder.
        d = os.getcwd()
        for path, subdirs, files in os.walk(d):
            for name in files:
                extracted_path = os.path.join(path, name)
                if ("sensed_data_json.txt" in extracted_path):
                    sensed_data_json_file = extracted_path
        
obj = staticVariable()

def updateSensedDataAsJson(sensedValues):
    print("entered update json")
    obj.liveData.append(sensedValues)
    with open(obj.sensed_data_json_file, 'w') as outfile:
        json.dump(obj.liveData, outfile)
    
    print("completed update json")

def getLiveData():
    print(os.name)
    with open(obj.sensed_data_json_file) as json_file:
        data = json.load(json_file)
        return data[-1]
