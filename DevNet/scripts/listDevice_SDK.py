from dnacentersdk import api


def main():
    """
    Execution begins here
    """

    #Create new DNAC object with connection creds and info
    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac2.cisco.com",
        username="devnetuser",
        password="Cisco123!",
        verify=False

    )

    # HTTP GET equivalent in SDK

    devices = dnac.devices.get_device_list()

    # Debugging Line; pretty-print JSON to see struct
    # import json; print(json.dumps(devices, indent=2))

    for device in devices['response']:
        print(f"ID: {device['id']}   IP: {device['managementIpAddress']}")


if __name__ == "__main__":
    main()