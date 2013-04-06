from gcm import gcm
import json
# import panstora.models


def getAPIKey():
    return open("apikey").read()


def sendSuggestion(regid, suggestion):
    conn = gcm.GCM(getAPIKey())
    # In the future, this will have to be changed
    data = json.dumps(suggestion)
    msg = gcm.JSONMessage(regid, data)
    ret = conn.send(msg)
    if ret.failed:
        pass
