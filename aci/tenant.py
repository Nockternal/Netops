import json
import requests
import urllib3
from login import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def tenant(APIC, username, password, TenantName, TenantAlias, Tenant_Descr):

    cookie = login(APIC,username,password)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    # https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-PythonTenantName.json
    url_prepend = 'node/mo/uni/tn-{TenantName}.json'.format(TenantName=TenantName)

    url = base_url + url_prepend

    headers = {
        'Content-Type': 'application/json',
        'Connection':'keep-alive'
    }
    prepayload = {
                    "fvTenant": {
                        "attributes": {
                        "dn": "uni/tn-{TenantName}".format(TenantName=TenantName),
                        "name": "{TenantName}".format(TenantName=TenantName),
                        "nameAlias": "{TenantAlias}".format(TenantAlias=TenantAlias),
                        "descr": "{Tenant_Descr}".format(Tenant_Descr=Tenant_Descr),
                        "rn": "tn-{TenantName}".format(TenantName=TenantName),
                        "status": "created, modified"
                        },
                        "children": []
                    }
                }
    payload = json.dumps(prepayload)

    response = requests.request(
        "POST",
        url,
        cookies=cookie,
        data=payload,
        headers=headers,
        verify=False
    )
    json_response = json.loads(response.text)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    return response.status_code

if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = 'ciscopsdt'
    TenantName = 'PythonTenants'
    TenantAlias = 'PythonTenantAlias'
    Tenant_Descr = 'This tenant was created using python'

    print(tenant(url, username, password, TenantName, TenantAlias, Tenant_Descr))