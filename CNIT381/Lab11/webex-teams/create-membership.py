# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests

access_token = '<redacted>'

room_id = '<redacted>'

person_email = '<redacted>'

url = 'https://webexapis.com/v1/memberships'

headers = {

    'Authorization':'Bearer {}'.format(access_token),
    'Content-Type':'application/json'

}

params = {'roomId':room_id, 'personEmail':person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())