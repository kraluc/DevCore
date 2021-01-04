import json
import requests
import logging

logging.basicConfig(filename='messenger.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('messenger')

# Bot Token is obtained from https://developer.webex.com/my-apps/vinnie-40377
BOT_TOKEN ='N2I4NTkxM2ItNWQyYi00YmU4LTliMTAtZDhjNGE1MDEwN2U5NmZmZmRmZmMtY2E3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
ACCESS_TOKEN='N2JiNGNlZTYtNmNhOC00YWY5LWFkNWQtYzYwZjc0YjVhNDExZjhkNzhmYTQtODU4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
# Webex teams messages API endpoint
WEBEXAPI_URL = 'https://webexapis.com/v1'  # see Doc https://developer.webex.com/docs/api/basics


class Messenger():
    def __init__(self, base_url=WEBEXAPI_URL, api_key=ACCESS_TOKEN):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-type": "application/json"
        }
        # Get the ID for the BOT associated with the base_url
        self.bot_id = requests.get(f'{self.base_url}/people/me', headers=self.headers).json().get('id')

    def list_messages(self, room_id) -> list:
        """ API 'List messages' in a room. TODO: handle pages>MAX """
        params = {
            "roomId": room_id
        }
        return requests.get(url=f'{self.base_url}/messages', headers=self.headers, params=params).json()['items']


    def get_message(self, message_id):
        """ Retrieve a specific message, specified by message_id. API 'Get Message Details'"""
        print(f'MESSAGE ID: {message_id}')
        receive_message_url = f'{self.base_url}/messages/{message_id}'
        self.message_text = requests.get(url=receive_message_url, headers=self.headers).json().get('text')


    def post_message(self, room_id, message: str):
        """ Post message to a Webex Teams space, specified by room_id """
        data = {
            "roomId": room_id,
            "text": message,
        }
        post_message_url = f'{self.base_url}/messages'
        post_message = requests.post(url=post_message_url, headers=self.headers, data=json.dumps(data))
        print(json.dumps(post_message.json(), indent=4))

if __name__ == "__main__":
    test_room = "Y2lzY29zcGFyazovL3VzL1JPT00vOGIwYTFkZjAtNDU0OC0xMWViLWEwYjktYTFhNTU1MzI0MzAw"
    client = Messenger()
    messages = client.list_messages(test_room)
    print('####  MESSAGES ####')
    for message in messages:
        print(json.dumps(message, indent=4))  # pretty print
