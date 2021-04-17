import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login(url,username,password):
    url = "https://{address}/api/aaaLogin.json".format(address=url)

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