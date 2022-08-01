import requests
import getToken


def addDevice():

    add_device_api_path = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

    add_device_auth = getToken.getToken()

    add_device_headers = {

        "Content-Type": "application/json",
        "X-Auth-Token": f"{add_device_auth}",
        "Accept": "application/json",

    }

    payload = {
        "snmpRetry": 10,
        "snmpTimeout": 20,
        "cliTransport": 'ssh',
        "enablePassword": 'Cisco123!',
        "ipAddress": ['10.1.1.1', '255.255.255.0']

    }

    response = requests.request(
        'POST', add_device_api_path, headers=add_device_headers, data=payload, verify=False)

    print(response.text.encode('utf-8'))


def main():
    addDevice()


if __name__ == "__main__":
    main()
