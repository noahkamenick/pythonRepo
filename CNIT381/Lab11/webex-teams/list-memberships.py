# Fill in this file with the membership code from the Webex Teams exercise
import requests

access_token = '<redacted>'

room_id = '<redacted>'

url = 'https://webexapis.com/v1/memberships'

headers = {

    'Authorization':'Bearer {}'.format(access_token),
    'Content-Type':'application/json'

}

params = {'room_id': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())