#!/usr/bin/python3


from telnetlib import AUTHENTICATION
import requests
import json

url = "https://api.smsafrica.tech/api/message/send/sms"

payload = {
        "sender_id": "FULUSI",
        "msisdn": "0792852100",
        "message": "Test"
}
headers = {
  'AUTHORIZATION': '',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

print(response.text.encode('utf8'))
