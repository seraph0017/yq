import requests
import json


TU_LING_URL = "http://openapi.turingapi.com/openapi/api/v2"
apiKey = "77e7030323c6cb7399c674d52f7e3f4d"
userId = "18616708172"



def dm_to_tuling(input_msg):
    result = ""
    perception = {
        "inputText": {
            "text": input_msg
        }
    }
    payload = {
        "reqType": 0,
        "perception": perception,
        "userInfo": {
            "apiKey": apiKey,
            "userId": userId 
        }
    }
    res = requests.post(TU_LING_URL, data=json.dumps(payload))
    for r in json.loads(res.content).get("results"):
        result+=r
    return result
