#!/bin/env python

import json, sys
import logging
import requests

DEBUG = False
LOGFILE = "meraki.log"
logging.basicConfig(filename=LOGFILE, encoding='utf-8', level=logging.INFO)
logger = logging.getLogger("meraki_operations")

## Logging Level
if DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

# Global variables for Sandbox
API_URL = "https://api.meraki.com/api/v0"
METHOD = "GET"
ORGANIZATION_ID = "681155"
NETWORK_ID = "L_783626335162466320"
SERIAL= "Q2KD-KWMU-7U92"
PAYLOAD={}
HEADERS = {
    'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

## Decorator function for requests.request - logs results and raise exceptions
def log(func):
    """ decorator function to log result and raise exceptions """
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            print(f"response code: {response.status_code}")
            if response.status_code == requests.codes.ok:
                print(json.dumps(response.json(), indent=4))
                logger.info(f"Successful!")
                return response
            else:
                response.raise_for_status()
        except Exception as err:
            logger.error(f"{err}")
            sys.exit(1)
    return wrapper

@log
def get_organizations():
    url = f"{API_URL}/organizations"
    return requests.get(url=url, headers=HEADERS, data=PAYLOAD)

@log
def get_organization_networks(organization_id: str = ORGANIZATION_ID):
    url = f"{API_URL}/organizations/{organization_id}"
    return requests.get(url=url, headers=HEADERS, data=PAYLOAD)

@log
def get_network_devices(network_id: str = NETWORK_ID):
    url = f"{API_URL}/networks/{network_id}/devices"
    return requests.get(url=url, headers=HEADERS, data=PAYLOAD)

@log
def get_network_info(network_id: str = NETWORK_ID):
    url = f"{API_URL}/networks/{network_id}"
    return requests.get(url=url, headers=HEADERS, data=PAYLOAD)

@log
def get_device_sn(network_id: str = NETWORK_ID, serial_number: str = SERIAL):
    url = f"{API_URL}/networks/{network_id}/devices/{SERIAL}"
    return requests.get(url=url, headers=HEADERS, data=PAYLOAD)

@log
def get_network_ssids(network_id: str = NETWORK_ID):
    url = f"{API_URL}/networks/{network_id}/ssids"
    return requests.get(url=url, headers=HEADERS, data=PAYLOAD)



if __name__ == "__main__":

    print('*** Organizations ***')
    get_organizations()
    print (f"\n\n*** Organization {ORGANIZATION_ID} Networks ***")
    get_organization_networks()
    print (f"\n\n*** Network {NETWORK_ID} Devices ***")
    get_network_devices()
    print (f"\n\n*** Network {NETWORK_ID} Info ***")
    get_network_info()
    print (f"\n\n*** Network {NETWORK_ID} Device SN {SERIAL} ***")
    get_device_sn()
    print (f"\n\n*** Network {NETWORK_ID} SSIDs ***")
    get_network_ssids()