import requests
from requests.auth import HTTPBasicAuth
from dnac_config import USERNAME, PASSWORD

requests.packages.urllib3.disable_warnings()

def get_auth_token():
    """
    Building out Auth Request. Using requests.post to make a call
    to the Auth Endpoint for DNAC

    """
    # Endpoint URL
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    # Make POST Request
    resp = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    # Retreive the Token from the returned JSON
    token = resp.json()['Token']
    # Print out the token 
    print("Token Retreived: {}".format(token))
    # Create a return statement to send the token back for later
    # use
    return token
    # Call the function that you have created and retreive
    # the Token
    
if __name__ == "__main__":
    get_auth_token()

