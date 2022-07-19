import requests
import json


def getToken():
    # Declare useful local vars
    api_path = "https://sandboxdnac2.cisco.com/dna"
    auth = ("devnetuser", "Cisco123!")
    headers = {"content-type": "application/json"}

    # Issue HTTP POST request
    auth_resp = requests.post(
        f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers, verify=False)

    # If success, print token. Else, raise HTTP error with details

    token = auth_resp.json()["Token"]
    return token


def main():
    token = getToken()
    print(token)


if __name__ == "__main__":
    main()
