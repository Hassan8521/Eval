#!/usr/bin/python3


from telnetlib import AUTHENTICATION
import requests
import json

url = "https://#/api/message/send/sms"

payload = {
        "sender_id": "",
        "msisdn": "",
        "message": "Test"
}
headers = {
  'AUTHORIZATION': '',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

print(response.text.encode('utf8'))
