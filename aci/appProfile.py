import json
import requests
import urllib3
from login import login


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def bd(
    APIC,
    username,
    password,
    TenantName,
    VrfName,
    BridgeDom,
    BdAlias,
    BdDesc,
    ArpFlood
    ):

    cookie = login(APIC, username, password)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    # node/mo/uni/tn-PythonTenant/BD-pyBd.json
    url_prepend = 'node/mo/uni/tn-{TenantName}/BD-{Bd}.json'.format(TenantName=TenantName, Bd=BridgeDom)
    url = base_url + url_prepend

    headers = {
        'Content-Type': 'application/json',
        'connection': 'keep-alive'
    }

    prepayload = {
                "fvBD": {
                    "attributes": {
                    "dn": "uni/tn-{TenantName}/BD-{Bd}".format(TenantName=TenantName, Bd=BridgeDom),
                    "name": "{Bd}".format(Bd=BridgeDom),
                    "nameAlias": "{BdAlias}".format(BdAlias=BdAlias),
                    "descr": "{BdDesc}".format(BdDesc=BdDesc),
                    "arpFlood": "{ArpFlood}".format(ArpFlood=ArpFlood.lower()),
                    "rn": "BD-{Bd}".format(Bd=BridgeDom),
                    "status": "created, modified"
                    },
                    "children": [
                    {
                        "fvRsCtx": {
                        "attributes": {
                            "tnFvCtxName": "{VrfName}".format(VrfName=VrfName),
                            "status": "created,modified"
                        },
                        "children": []
                        }
                    }
                    ]
                }
            }


    payload = json.dumps(prepayload)

    response = requests.request(
        'POST',
        url,
        cookies=cookie,
        data=payload,
        headers=headers,
        verify=False
    )
    json_response = json.loads(response.text)
    return response.status_code


if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = 'ciscopsdt'
    tenantName = 'PythonTenant'
    VrfName = 'pyVrf'
    BridgeDom = 'pyBd'
    BdAlias = 'pyBd_Alias'
    BdDesc = 'pyBd_Desc'
    ArpFlood = 'True'

    print(bd(
        url,
        username,
        password,
        tenantName,
        VrfName,
        BridgeDom,
        BdAlias,
        BdDesc,
        ArpFlood
    ))