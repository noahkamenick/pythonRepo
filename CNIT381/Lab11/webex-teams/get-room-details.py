# Fill in this file with the code to get room details from the Webex Teams exercise
import requests

access_token = '<redacted>'

room_id = '<redacted>'

url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)

headers = { 

    'Authorization':'Bearer {}'.format(access_token),
    'Content-Type':'application/json'

}

res = requests.get(url, headers=headers)
print(res.json())

