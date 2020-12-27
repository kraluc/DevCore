#    Operations with always-on DNA Center sandbox
#
#    *  sandbox topology:
#       https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology
#    *  Access details
#       Go to https://sandboxdnac2.cisco.com
#       Login with credentials [devnetuser/Cisco123!]

import requests

def get_token():
    """
    Gets an access token from Cisco DNA Center always-on sandbox. Returns the token
    string if successful; False otherwise
    """

    # Declare Useful local variabales to simplify request process
    api_path = "https://sandboxdnac.cisco.com/dna"
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-type": "application/json"}

    # Issue http POST request to the proper URL to request a token
    auth_resp = requests.post(
        f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers
    )

    # If successful, print token. Else, raise HTTPError with details
    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token

def main():
    """
    Execution begins here
    """

    token = get_token()
    print(token)


if __name__ == "__main__":
    main()
