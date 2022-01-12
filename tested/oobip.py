import json
import requests
import urllib3
from aci_login import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def oob_ip_post(
        APIC,
        loginuser,
        password,
        NodeID,
        PodID,
        OOB_IP,
        MASK,
        Gateway
):

    cookies = login(APIC, loginuser, password)
    print(cookies)
    
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    # node/mo/uni/tn-mgmt/mgmtp-default/oob-default/rsooBStNode-[topology/pod-1/node-101].json
    # https://10.10.20.14/api/node/mo/uni/tn-mgmt/mgmtp-default/oob-default/rsooBStNode-[topology/pod-1/node-101].json
    url_prepend = "node/mo/uni/tn-mgmt/mgmtp-default/oob-default/rsooBStNode-[topology/pod-{PodID}/node-{NodeID}].json".format(PodID=PodID, NodeID=NodeID)

    url = base_url + url_prepend

    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive"
    }
    prepayload = {
                    "mgmtRsOoBStNode": {
                        "attributes": {
                        "tDn": "topology/pod-{PodID}/node-{NodeID}".format(PodID=PodID, NodeID=NodeID),
                        "addr": "{OOB_IP}/{MASK}".format(OOB_IP=OOB_IP, MASK=MASK),
                        "gw": "{Gateway}".format(Gateway=Gateway),
                        "status": "created"
                        },
                        "children": []
                    }
                }

    payload = json.dumps(prepayload)
    print(json.dumps(payload, indent=4, sort_keys=True))

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
    # url = 'sandboxapicdc.cisco.com'
    url = '10.10.20.14'
    username = 'admin'
    # password = 'ciscopsdt'
    password = 'C1sco12345'
    NodeID = '101'
    PodID = '1'
    OOB_IP = '10.10.20.101'
    MASK = '24'
    Gateway = '10.10.20.254'
    oob_ip_post(url, username, password, NodeID, PodID, OOB_IP, MASK,Gateway)