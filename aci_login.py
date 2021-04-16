import requests
import json


def login(url,username,password):
    url = "https://{url}/api/aaaLogin.json".format(url=url)

    prepayload={
        "aaaUser": {
            "attributes": {
                "name": "admin", 
                "pwd": "ciscopsdt"}
            }
        }
    headers = {
    'Content-Type': 'application/json'
    }
    payload = json.dumps(prepayload)
    response = requests.request(
        "POST", 
        url, 
        headers=headers, 
        data=payload, 
        timeout=2, 
        verify=False)
    data = json.loads(response.text)
    return data['imdata'][0]['aaaLogin']['attributes']['token']
      
if __name__ == '__main__':
    username = 'admin'
    password = 'ciscopsdt'
    url = 'sandboxapicdc.cisco.com'
    cookie = login(url,username,password)
    print(cookie)