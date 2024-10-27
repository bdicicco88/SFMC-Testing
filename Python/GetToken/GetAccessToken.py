import requests
import json
import random
import time
import uuid
import pyperclip

Clientid = ""
ClientSecret = ""
tse = ""


api_Auth_url = "https://" + tse + ".auth.marketingcloudapis.com/v1/requestToken?legacy=1"

payload = json.dumps({"clientId": Clientid, "clientSecret": ClientSecret})
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", api_Auth_url, headers=headers, data=payload)
#Get Token
jsonresponse = response.json()
accessToken = jsonresponse['accessToken']

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
    }

print("This is the Access Token: " + accessToken + "Has been copied to clipboard")

pyperclip.copy(accessToken)
