import json
import requests
import urllib3
from login import login


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def vrf(
    APIC,
    username,
    password,
    TenantName,
    VrfName,
    VrfAlias,
    VrfDescription,
    PolEnforment='enforced'
    ):

    cookie = login(APIC, username, password)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    # node/mo/uni/tn-PythonTenant.json
    url_prepend = 'node/mo/uni/tn-{TenantName}.json'.format(TenantName=TenantName)
    url = base_url + url_prepend

    headers = {
        'Content-Type': 'application/json',
        'connection': 'keep-alive'
    }

    prepayload = {
            "fvTenant": {
                "attributes": {
                "dn": "uni/tn-{TenantName}".format(TenantName=TenantName),
                "status": "modified"
                },
                "children": [
                {
                    "fvCtx": {
                    "attributes": {
                        "dn": "uni/tn-{TenantName}/ctx-{VrfName}".format(TenantName=TenantName, VrfName=VrfName),
                        "name": "{VrfName}".format(VrfName=VrfName),
                        "nameAlias": "{VrfAlias}".format(VrfAlias=VrfAlias),
                        "descr": "{VrfDescription}".format(VrfDescription=VrfDescription),
                        "pcEnfPref": "{PolEnforment}".format(PolEnforment=PolEnforment),
                        "rn": "ctx-{VrfName}".format(VrfName=VrfName),
                        "status": "created, modified"
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
    vrfName = 'pyVrf'
    vrfAlias = 'pyVrf_Alias'
    vrfDescr = 'pyVrf_Desc'
    PolEnforment = 'unenforced'

    print(vrf(
        url,
        username,
        password,
        tenantName,
        vrfName,
        vrfAlias,
        vrfDescr,
        PolEnforment
    ))

