# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json

access_token = '<redacted>'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization':'Bearer {}'.format(access_token)
}
res = requests.get(url,headers=headers)
print(json.dumps(res.json(), indent=4))

