#!/bin/env python
#
#   Webex_operations.py
#
#   v1.0
#   Vincent Ricci
#
#   Need to update the TOKEN (12h valid)
#   Methods to list spaces user is a member of (based on TOKEN)
#   Extract the title lists
#   Extract room / room ID for one space based on title

#   TODO: May want to turn this into a class + Cache results


import sys
import requests
import logging
import json

logging.basicConfig(filename="requests.log", encoding='utf-8', level=logging.INFO)
logger = logging.getLogger("webex_operations")

## GLOBAL VARIABLES
TOKEN="YTI5NjkyMmItYmRkNy00NTM4LWE3N2YtOTE5YjJkYzNiZmVhZmIwYmY1MGItYzI5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"  # This Token needs to be renewed every 12hr
API_URL="https://webexapis.com/v1"  # Webex API URL
HEADERS = {
    "Authorization": f'Bearer {TOKEN}',
    "Content-Type": "application/json"
}

PAYLOAD = {}
DEBUG = False
LOGFILE = "requests.log"

## Logging Level
if DEBUG == True:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)


## Decorator function for requests.request - logs results and raise exceptions
def log(request):
    """ decorator function to log result and raise exceptions """
    def wrapper(*args, **kwargs):
        try:
            response = request(*args, **kwargs)
            if response.status_code == requests.codes.ok:
                logger.info(f"Successful!")
                return response
            else:
                response.raise_for_status()
        except Exception as err:
            logger.error(f"{err}")
            sys.exit(1)
    return wrapper


# refactor requests.request to include logging and exception handling
@log
def request(*args, **kwargs):
    """ returns requests.request """
    return requests.request(*args, **kwargs)


# List of Webex Rooms that user (TOKEN) is a member of
def get_rooms(method:str="GET", api_url:str=API_URL, urn:str="rooms")-> list:
    """ returns a list of Webex team spaces (aka rooms) in JSON format """
    response = request(method,url=f"{api_url}/{urn}", headers=HEADERS, data=PAYLOAD)
    return response.json()['items']


#  Extract the list of space titles
def room_titles(spaces:list)->list:
    titles = [ room['title'] for room in spaces]
    return titles


# Pretty print a JSON object
def pretty_print(json_object:dict, sort_keys=False, indent:int=4):
    print(json.dumps(json_object, sort_keys=sort_keys, indent=indent))


# Extract room matching title from list of spaces
def extract_space_with_title(title:str, spaces:list)->dict:
    """ returns JSON output associated with particular space title """
    # obtains the list of rooms (each room is a dictionary)
    for room in spaces:
        if title in room.values():
            logger.info(f"extract_space_with_title: found space entitled {title}")
            return room
    logger.warning(f"extract_space_with_title: no space entitled {title} found")
    return {}


def main():
    ## Get spaces
    spaces = get_rooms()
    print('### ROOMS ###')
    titles = room_titles(spaces)
    print(type(titles))
    print(dir(titles))
    sorted_titles = titles.sort()
    print(sorted_titles)

    ## Extract JSON space based on title
    title = "Test Space"
    my_room = extract_space_with_title(title, spaces)
    roomId = my_room['id']
    print (f"### ROOM '{title}' ###")
    pretty_print(my_room)
    print(f'\nroomId: {roomId}')


if __name__ == "__main__":
    main()
