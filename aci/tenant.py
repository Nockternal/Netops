import json
import requests
import urllib3
from login import login


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def tenant(
    APIC,
    username,
    password,
    TenantName,
    TenantAlias,
    TenantDescription):

    cookie = login(APIC, username, password)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    # node/mo/uni/tn-AlphaTenant.json
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
            "name": "{TenantName}".format(TenantName=TenantName),
            "nameAlias": "{TenantAlias}".format(TenantAlias=TenantAlias),
            "descr": "{TenantDescription}".format(TenantDescription=TenantDescription),
            "rn": "tn-{TenantName}".format(TenantName=TenantName),
            "status": "created"
            },
            "children": []
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
    tenantAlias = 'PythonTenant_Alias'
    tenantDescr = 'PythonTenant_Desc'

    print(tenant(
        url, username, password, tenantName, tenantAlias, tenantDescr
    ))