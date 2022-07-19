from auth import get_auth_token
import requests 
from printDeviceList import print_device_list

token = get_auth_token() # Get a token

url = "https://sandboxdnac.cisco.com/api/v1/network-device" # Network Device Endpoint

hdr = {'x-auth-token': token, 'content-type' : 'application/json'} # Build header info

queryString = {"role" : "DISTRIBUTION"} # Query devices based on objects keys/values

resp = requests.get(url, headers=hdr, params=queryString) # Make the GET request

device_list = resp.json() # Capture the data from the controller

print("--------------------------------------------------") # Formatting String

print_device_list(device_list) # Pretty Print data