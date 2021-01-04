#!/usr/bin/env python
#
#   Webex_operations_sdk.py
#
#   v1.0
#   Vincent Ricci
#
#   This is an attempt to rewrite Webex_operations.py using the webexteamssdk
#   [quickstart](https://webexteamssdk.readthedocs.io/en/latest/user/quickstart.html)
#
#      *  webexteamssdk defaults to pulling your Webex Teams access token
#             from a WEBEX_TEAMS_ACCESS_TOKEN environment variable
#      *  Methods to list spaces user is a member of (based on TOKEN)
#      *  Extract the title lists
#      *  Extract room / room ID for one space based on title
import logging
from webexteamssdk import WebexTeamsAPI

logging.basicConfig(filename="requests.log", encoding='utf-8', level=logging.INFO)
logger = logging.getLogger("webex_operations")

## Logging Level
DEBUG = False
LOGFILE = "requests.log"

if DEBUG == True:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

## Main
api = WebexTeamsAPI()

def main():
    ''' straight from the README posted on https://github.com/Devnet/webexteamssdk '''
    # demo_rooms: find all the rooms that have 'Test Space' in the title
    title = 'Test Space'
    all_rooms = api.rooms.list()
    demo_rooms = [room for room in all_rooms if f"{title}" in room.title]

    for room in demo_rooms:
        msg = f'found {room.title} with rooomID {room.id}'
        print(msg)
        logger.info(msg)

    # Delete all the demo rooms
    for room in demo_rooms:
        api.rooms.delete(room.id)
        msg = f'deleted room {room.title}'
        logger.info(msg)
        print(msg)

    # Create a demo room
    demo_room = api.rooms.create(title)

    # Add people to the new demo room
    email_addresses = ['ToFrench@webex.bot', 'vinniebot@webex.bot']
    for email in email_addresses:
        msg = f'user {email} added to {demo_room.title}'
        api.memberships.create(
            demo_room.id,
            personEmail=email,
            text="Welcome to the room!",
            files=["https://www.webex.com/content/dam/wbx/us/images/dg-integ/teams_icon.png"])
        print(msg)
        logger.info(msg)

if __name__ == "__main__":
    main()
