from gcm import gcm
import json
# import panstora.models

print gcm.GCM_URL


def getAPIKey():
    return open("apikey").read()


def sendSuggestion(regid, suggestion):
    conn = gcm.GCM(getAPIKey())
    msg = gcm.JSONMessage(regid, json.dumps(suggestion))
    ret = conn.send(msg)
