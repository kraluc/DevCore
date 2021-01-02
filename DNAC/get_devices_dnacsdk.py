#!/usr/bin/env python

#    Operations with always-on DNA Center sandbox
#
#    *  sandbox topology:
#       https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology
#    *  Access details
#       Go to https://sandboxdnac2.cisco.com
#       Login with credentials [devnetuser/Cisco123!]

from dnacentersdk import api

def main():
    """
    Execution begins here
    """

    # Create DNAC object, which automatically handles the token request process
    # API docs in the link below, which may change:
    # https://dnacentersdk.readthedocs.io/en/latest/api/api.html

    dnac = api.DNACenterAPI(
        base_url="https://sandboxdnac2.cisco.com",
        username="devnetuser",
        password="Cisco123!",
    )

    # Use the devices.get_device_list() method to get  a list of devices,
    # which is equivalent to the manual HTTP GET in the previous course
    devices = dnac.devices.get_device_list()

    # Debugging line; pretty-print JSON to see structure
    #import json ; print(json.dumps(devices, indent=2))

    # Same exact loop from previous course, just get the device ID
    # and management IP address printed in a single neat row
    for device in devices["response"]:
        print(f"ID: {device['id']} IP: {device['managementIpAddress']}")

if __name__ == "__main__":
    main()

