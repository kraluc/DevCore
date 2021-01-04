from flask import Flask, request, json
from flask.helpers import get_flashed_messages
import requests
from werkzeug import datastructures
from messenger import Messenger  # Nested Module
import logging

# Set logging level
logging.basicConfig(filename='chatbox.log', encoding='utf-8',  level=logging.INFO)
logger = logging.getLogger('chatbox')

app = Flask(__name__)
port = 5005

msg = Messenger()

@app.route('/', methods=['GET', 'POST'])
def index():
    """ Receive a notification from Webex Teams and handle it"""
    if request.method == 'GET':
        log_msg = f"Request received on local port {port}"
        logger.info(log_msg)
        return log_msg

    elif request.method == 'POST':
        if 'application/json' in request.headers.get('Content-Type'):
            # Notification payload, received from Webex Teams Webhook
            data = request.get_json()

            # Loop prevention, ignore messages which were posted by bot itself.
            # The bot id attribute is collected from the Webex Teams API
            # at object instantiation.
            if msg.bot_id == data.get('data').get('personId'):
                message = 'Message from self ignored'
                logger.info = message
                return message
            else:
                # Print the notification payload, received from the webhook
                print(json.dumps(data, indent=4))

                # Collect the roomID from the notification
                # so you know where to post the response
                # Set the msg object attribute
                msg.room_id = data.get('data').get('roomId')

                # Collect the message id from the notification
                # so you can fetch the message content.
                message_id = data.get('data').get('id')

                # Get the contents of the received message.
                msg.get_message(message_id)

                # If message starts with '/server', relay it to the web server.
                # if not, just post a confirmation that a message was received.
                if msg.message_text.startswith('/server'):
                    # Default action is to list send the 'stats' command
                    try:
                        action = msg.message_text.split()[1]
                    except IndexError:
                        action = 'status'

                    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                    data = f'action={action}'
                    web_server = 'http://dev.web.local/status'
                    msg.reply = requests.post(web_server, headers=headers, data=data).text
                    msg.post_message(msg.room_id, msg.reply)
                else:
                    msg.reply = f'Bot received message"{msg.message_text}"'
                    msg.post_message(msg.room_id, msg.reply)

                return data
        else:
            log_msg = 'Wrong data format'
            logger.error(log_msg)
            return (log_msg, 400)


if __name__ == '__main__':

    def get_ngrok_urls():
        urls = ['https://fcea92ae526d.ngrok.io']        # Must update this URL with running ngrok URL
        ngrok_console = 'http://127.0.0.1:4040/api/tunnels'
        try:
            tunnels = requests.get(ngrok_console).json()['tunnels']
        except Exception:
            print('NGROK NOT RUNNING')
            print("Run ngrok by opening a new terminal window and typing ngrok httop 5005")
            exit(0)

        for tunnel in tunnels:
            urls.append(tunnel['public_url'])
        return urls

    def get_webhook_urls():
        webhook_urls = []
        webhooks_api = f'{msg.base_url}/webhooks'
        webhooks = requests.get(webhooks_api, headers=msg.headers)
        if webhooks.status_code != 200:
            webhooks.raise_for_status()
        else:
            for webhook in webhooks.json()['items']:
                webhook_urls.append(webhook['targetUrl'])
        return webhook_urls

    def create_webhook(url):
        webhooks_api = f'{msg.base_url}/webhooks'
        data = {
            "name": "Webhook to ChatBot",
            "resource": "all",
            "event": "all",
            "targetUrl": f"{url}"
        }
        webhook = requests.post(webhooks_api, headers=msg.headers, data=json.dumps(data))
        if webhook.status_code != 200:
            webhook.raise_for_status()
        else:
            message = f'Webhook to {url} created'
            logger.info(message)
            print(message)

        ngrok_urls = get_ngrok_urls()
        webhook_urls = get_webhook_urls()

        intersect = list(set(ngrok_urls) & set(webhook_urls))
        if intersect:
            message = f'Registered Webhook: {intersect[0]}'
            logger.info(message)
            print(message)
        else:
            logger.info(f'Creating webhook {ngrok_urls[0]}')
            create_webhook(ngrok_urls[0])
        logger.info('starting server app')
        app.run(host='0.0.0.0', port=port, debug=True)