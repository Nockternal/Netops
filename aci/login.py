import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login(url, username, password):
    base_url = 'https://{ApicUrl}/api/'.format(ApicUrl=url)
    # create credentials structure
    prepayload = {
        'aaaUser': 
            {'attributes': 
                {'name': '{username}'.format(username=username), 
                'pwd': '{password}'.format(password=password)
                }
            }
        }
    payload = json.dumps(prepayload)
    # log in to API
    url = base_url + 'aaaLogin.json'
    headers = {
        'content-type': 'application/json'
    }
    try:
        response = requests.request(
            'POST',
            url,
            headers=headers,
            data=payload,
            timeout=2,
            verify=False
        )
        data = json.loads(response.text)
        token = {}
        token['APIC-Cookie']= data["imdata"][0]["aaaLogin"]["attributes"]["token"]
        #print(json.dumps(data, indent=4, sort_keys=True))
        return token
    except:
        print('Error occured')
    

if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = 'ciscopsdt'
    print(login(url, username, password))