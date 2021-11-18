# Fill in this file with the messages code from the Webex Teams exercise
import requests

access_token = '<redacted>'

room_id = '<redacted>'

message = 'Hello **DevNet Associate**!!'

url = 'https://webexapis.com/v1/messages'

headers = {

    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type':'application/json'

}

params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())