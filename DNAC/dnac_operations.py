#    Operations with always-on DNA Center sandbox
#
#    *  sandbox topology:
#       https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology
#    *  Access details
#       Go to https://sandboxdnac2.cisco.com
#       Login with credentials [devnetuser/Cisco123!]

#!/usr/bin/env python

import logging, sys
import requests
from requests.models import HTTPError


#  Logging Parameters
logging.basicConfig(
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
#    stream=sys.stdout,
    filename=f"{__file__.split('.')[0]}.log",
    filemode='a',
    level=logging.INFO
    )
logger = logging.getLogger(__name__)

DEBUG = False
if DEBUG:
    logger.setLevel(level=logging.DEBUG)
else:
    # attribute level expects an integer --> logging.INFO
    # >>> type(logging.info)
    # <type 'function'>
    # >>> type(logging.INFO)
    # <type 'int'>
    logger.setLevel(level=logging.INFO)

# Default Credentials as published on https://sandboxdnac2.cisco.com
AUTH = ("devnetuser", "Cisco123!")


def get_token(username: str = AUTH[0], password: str = AUTH[1]):
    """
    Gets an access token from Cisco DNA Center always-on sandbox. Returns the token
    string if successful; False (None) otherwise
    """

    # Declare Useful local variabales to simplify request process
    api_path = "https://sandboxdnac.cisco.com/dna"
    auth = (username, password)
    #
    headers = {"Content-type": "application/json"}

    # Issue http POST request to the proper URL to request a token
    # If successful, print token. Else, raise HTTPError with details
    try:
        auth_resp = requests.post(
            f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers
        )
        auth_resp.raise_for_status()
        logger.info(msg=f"Successful POST - {auth_resp.status_code}")
        token = auth_resp.json()["Token"]
        return token

    except HTTPError as err:
        logger.error(msg=err)
        raise err


def main():
    """
    Execution begins here
    """

    token = get_token()
    print(token)
    print(len(token))


if __name__ == "__main__":
    main()
