import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
Modify these please
"""
# For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
# For basic authentication using username & pwd, set 'client_cert_auth' to False.
client_cert_auth = False

# Fill in the device IP and credentials
switchuser = ''
switchpassword = ''
url = 'https://<ip-address>/ins'

myheaders = {'content-type': 'application/json-rpc'}
payload = [
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show int eth1/1",
            "version": 1
        },
        "id": 1
    }
]

if client_cert_auth is False:
    try:
        response = requests.post(url, data=json.dumps(
            payload), headers=myheaders, auth=(switchuser, switchpassword)).json()
    except Exception as e:
        print(str(e))