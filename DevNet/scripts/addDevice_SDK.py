from asyncio import tasks
import time
from dnacentersdk import api


def main():
    """
    Execution begins here
    """

    # Create new DNAC object with connection creds and info
    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac2.cisco.com",
        username="devnetuser",
        password="Cisco123!",
        verify=False

    )

    new_device_dict = {  # Necessary dictionary key/values to make successful post

        "ipAddress": ["192.168.2.1"],
        "snmpVersion": "v2",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": 1,
        "snmpTimeout": 60,
        "cliTransport": "ssh",
        "userName": "noah",
        "password": "secret123!",
        "enablePassword": "secret456!",

    }

    add_data = dnac.devices.add_device(**new_device_dict)

    # Debugging Line; pretty-print JSON to see struct
    # import json; print(json.dumps(devices, indent=2))

    # Wait 10 seconds and get the async task ID, because this is asynchronous
    time.sleep(10)
    task = add_data["response"]["taskId"]
    task_data = dnac.task.get_task_by_id(task)

    # Debugging Line; pretty-print JSON to see struct
    # import json; print(json.dumps(devices, indent=2))

    if not task_data["response"]["isError"]:
        print("New device successfully added")

    else:
        print(f"Async task error: {task_data['progress']}")


if __name__ == "__main__":
    main()
