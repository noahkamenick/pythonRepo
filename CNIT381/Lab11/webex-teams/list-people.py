# Fill in this file with the people listing code from the Webex Teams exercise
import requests
import json

access_token = '<redacted>'
person_id = '<redacted>'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {

    'Authorization':'Bearer {}'.format(access_token),
    'Content-Type':'application/json'

}

params = {

    'email':'noahkamenick@gmail.com'

}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))


