import json
import requests
import urllib3
from login import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def preRegisterNode(
        APIC,
        loginuser,
        password,
        SERIAL,
        NODE_NAME,
        NODE_ID,
        POD_ID
):

    cookies = login(APIC, loginuser, password)
    print(cookies)
    
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    # https://sandboxapicdc.cisco.com/api/node/mo/uni/controller/nodeidentpol/nodep-AAAAAAAAAAAA.json
    url_prepend = "node/mo/uni/controller/nodeidentpol/nodep-{SERIAL}.json" .format(SERIAL=SERIAL)

    url = base_url + url_prepend

    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive"
    }
    prepayload = {
        "fabricNodeIdentP": {
            "attributes": {
            "dn": "uni/controller/nodeidentpol/nodep-{SERIAL}".format(SERIAL=SERIAL),
            "podId": "{POD_ID}".format(POD_ID=POD_ID),
            "serial": "{SERIAL}".format(SERIAL=SERIAL),
            "nodeId": "{NODE_ID}".format(NODE_ID=NODE_ID),
            "name": "{NODE_NAME}".format(NODE_NAME=NODE_NAME),
            "rn": "nodep-{SERIAL}".format(SERIAL=SERIAL),
            "status": "created"
            },
            "children": []
        }
    }

    payload = json.dumps(prepayload)
    #print(json.dumps(payload, indent=4, sort_keys=True))

    response = requests.request("POST",
                                url,
                                cookies=cookies,
                                data=payload,
                                headers=headers,
                                verify=False)
    print(response.status_code)
    json_response = json.loads(response.text)
    
    return json_response
    
if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = 'ciscopsdt'
    serial = 'DDDDDDDDDDDD'
    nodeName = 'FakeLeaf-230'
    nodeId = '230'
    podId = '2'
    preRegisterNode(
        url, 
        username, 
        password, 
        serial, 
        nodeName, 
        nodeId, 
        podId)