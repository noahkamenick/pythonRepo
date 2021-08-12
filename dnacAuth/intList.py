import requests
from intInfo import print_interface_info
from auth import get_auth_token

def get_device_int(device_id):
    """
    Building out function to retreive device interface. Using requests.get
    to make a call to the network device Endpoint
    """
    # Sandbox URL for int
    url = "https://sandboxdnac.cisco.com/api/v1/interface"
    # Generate Auth Token and assign
    token = get_auth_token()
    # Configure Headers
    hdr = {'x-auth-token': token, 'content-type': 'application/json'}

    queryString = {'macAddress':  device_id} # Dynamically build the query
    # params to get device-specific Interface info

    resp = requests.get(url, headers=hdr, params=queryString)
    # Make the GET request

    # Store response as JSON
    interface_info_json = resp.json()

    # Run method

    print_interface_info(interface_info_json)


if __name__ == "__main__":
        get_device_int('aa0a5258-3e6f-422f-9c4e-9c196db115ae')