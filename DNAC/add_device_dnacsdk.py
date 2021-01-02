#!/usr/bin/env python

"""
Author: Nick Russo (from pluralsight course)
Purpose: Basic consumption of the Cisco Digital Network Architecture
(DNA) Center software development kit (SDK) to add a new device
comparable flow to the HTTP POST and asynt HTTP GET used in the
previous course
"""

import time
from dnacentersdk import api

def main():
    """
    Execution begins here
    """

    # Create DNAC object, which automatically handles the token
    # request process. API docs in the link below, which may change:
    # https://dnacentersdk.readthedocs.io/en/latest/api/api.html
    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac2.cisco.com",
        username="devnetuser",
        password="Cisco123!",
    )

    # New device to add, same information as previous course
    new_device_dict = {
        "cliTransport": "ssh",
        "enablePassword": "test456!",
        "ipAddress": ["10.10.20.100"],
        "password": "test123!",
        "snmpVersion": "v3",
        "snmpAuthPassphrase": "blahblah",
        "snmpAuthProtocol": "sha",
        "snmpMode": "AuthenticationandPrivacy",
        "snmpPrivPassphrase": "blahblah",
        "snmpPrivProtocol": "aes128",
        "snmpROCommunity": "readonly",
        "snmpRWCommunity": "readwrite",
        "snmpRetry": 3,
        "snmpTimeout": 5,
        "snmpUserName": "vincent",
        "userName": "vincent",
    }

    # Unpack the new device dictionary into keyword arguments (kwargs)
    # and pass into the SDK. This also performs data validation, so if we
    # have the wrong data or miss a required fields, it tells us.
    add_data = dnac.devices.add_device(**new_device_dict)

    # debugging line; pretty-print JSON to see structure
    # import json ; print(json.dumps(add_data, indent=2))

    # Wait 10 seconds and get the async TASK ID
    time.sleep(10)
    task = add_data["response"]["taskId"]
    task_data = dnac.task.get_task_by_id(task)

    # Debugging line; pretty-print JSON to see structure
    # import json ; print(json.dumps(task_data, indent=2))

    # Ensure async task completed successfully
    if not task_data["response"]["isError"]:
        print("New device successfully added")
    else:
        print(f"Async task error seen: {task_data['progress']}")

if __name__ == "__main__":
    main()