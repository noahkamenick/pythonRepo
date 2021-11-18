import json
import requests
from requests.models import Response
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.102/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json",
"Content-type":"application/yang-data+json"
} ## Headers going into the request

basicauth = ("cisco", "cisco123!") ## Tuple for credentials

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

print(resp) 

## Format and display the JSON data received from the router

response_json = resp.json()

print(response_json)

## Prettify output

print(json.dumps(response_json, indent=4))

