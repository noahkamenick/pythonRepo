
import json
import requests
from getToken import getToken
import pprint


def getBody():

    # Create path vars, auth key, and define headers

    device_api_path = "https://sandboxdnac2.cisco.com/dna"
    toke = getToken()
    device_headers = {

        "Content-Type": "application/json",
        "X-Auth-Token": toke  # use this, DO NOT USE AUTHORIZATION

    }

    # Create GET Request

    resp = requests.get(f"{device_api_path}/intent/api/v1/network-device",
                        headers=device_headers, verify=False)

    # Raise error if fail, otherwise, extract information

    resp.raise_for_status()
    body = resp.json()
    return body


def getDeviceIPandID(jsonBody): 
    ip = jsonBody

    for loopIndex in range(len(ip['response'])):
        print(ip['response'][loopIndex]["managementIpAddress"] +
              " -> " + ip['response'][loopIndex]['id']) #Format ip and id


def main():
    deviceList = getBody()
    print(json.dumps(deviceList, indent=2)) #Pretty print json payload into terminal
    getDeviceIPandID(deviceList)


if __name__ == "__main__":
    main()
