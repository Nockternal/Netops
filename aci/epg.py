import json
import requests
import urllib3
from login import login


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def epg(
    APIC,
    username,
    password,
    TenantName,
    AppProfName,
    EpgName,
    EpgAlias,
    EpgDesc,
    BdName,
    FloodEncap='disabled'
    
    ):

    cookie = login(APIC, username, password)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    # node/mo/uni/tn-PythonTenant/ap-pyAppProfWeb/epg-pyEpg.json
    url_prepend = 'node/mo/uni/tn-{TenantName}/ap-{AppProfName}/epg-{EpgName}.json'.format(
        TenantName=TenantName, 
        AppProfName=AppProfName,
        EpgName=EpgName
        )
    url = base_url + url_prepend

    headers = {
        'Content-Type': 'application/json',
        'connection': 'keep-alive'
    }

    prepayload = {
        "fvAEPg": {
            "attributes": {
            "dn": "uni/tn-{TenantName}/ap-{AppProfName}/epg-{EpgName}".format(TenantName=TenantName,AppProfName=AppProfName,EpgName=EpgName),
            "name": "{EpgName}".format(EpgName=EpgName),
            "nameAlias": "{EpgAlias}".format(EpgAlias=EpgAlias),
            "descr": "{EpgDesc}".format(EpgDesc=EpgDesc),
            "floodOnEncap": "{FloodEncap}".format(FloodEncap=FloodEncap.lower()),
            "rn": "epg-{EpgName}".format(EpgName=EpgName),
            "status": "created, modified"
            },
            "children": [
            {
                "fvRsBd": {
                "attributes": {
                    "tnFvBDName": "{BdName}".format(BdName=BdName),
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
    AppProfName = 'pyAppProfWeb'
    EpgName = 'pyEpgWebFeWeb'
    EpgAlias = 'pyEpgWebFeWeb_Alias'
    EpgDesc = 'Frond End end point group servers'
    BdName = 'pyBd'
    FloodEncap='enabled'
    

    print(epg(
        url,
        username,
        password,
        tenantName,
        AppProfName,
        EpgName,
        EpgAlias,
        EpgDesc,
        BdName,
        FloodEncap
    ))