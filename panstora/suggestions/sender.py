from gcm import gcm
import json


def getAPIKey():
    ''' Read the API key from the "config" file '''
    return open("apikey").read()


def getTitle(sugg):
    ''' Generate a title based on information about the suggestion '''
    if sugg.suggType == "sale":
        return "Sale!"
    else:
        return "Suggested item".format(sugg.name)


def getMessage(sugg):
    ''' Generate a message based on information about the suggestion '''
    if sugg.suggType == "sale":
        return "{} is on sale for {}".format(sugg.name, sugg.price)
    else:
        return "{} is ".format(sugg.name)


def getImage(sugg):
    return ""


def sendSuggestion(regid, suggestion):
    ''' Send a suggestion to the user's device '''
    conn = gcm.GCM(getAPIKey())
    # In the future, this will have to be changed
    data = json.dumps({
        "title": getTitle(suggestion),
        "message": getMessage(suggestion),
        "image": getImage(suggestion)
    })
    msg = gcm.JSONMessage(regid, data)
    ret = conn.send(msg)
    if ret.failed:
        # Not sure if we even need to handle this
        pass
