import json
import requests
import urllib3
from aci_login import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def create_Tenant(
        APIC,
        loginuser,
        password,
        TENANT,
        TENANT_Alias,
        Tenant_Descr
):

    cookies = login(APIC, loginuser, password)
    print(cookies)
    
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    url_prepend = "node/mo/uni/tn-{TENANT}.json" .format(TENANT=TENANT)

    url = base_url + url_prepend

    headers = {
        'Content-Type': "application/json",
        'Connection': "keep-alive"
    }
    prepayload = {
        "fvTenant":
            {"attributes":
                {"dn": "uni/tn-{TENANT}" .format(TENANT=TENANT),
                 "name": "{TENANT}" .format(TENANT=TENANT),
                 "nameAlias": "{TENANT_Alias}".format(TENANT_Alias=TENANT_Alias),
                 "descr": "{Tenant_Descr}".format(Tenant_Descr=Tenant_Descr),
                 "rn": "tn-{TENANT}" .format(TENANT=TENANT),
                 "status": "created,modified"
                 },
             "children": []
             }
    }

    payload = json.dumps(prepayload)
    # print(json.dumps(payload, indent=4, sort_keys=True))

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
    #cookie = login(url,username,password)
    TENANT = 'pythonTenant'
    TENANT_Alias = 'PyTenant'
    Tenant_Descr = 'this tenant was create by python'
    create_Tenant(url, username, password, TENANT, TENANT_Alias, Tenant_Descr)