import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login(url, username, password):
    base_url = 'https://{apicAddress}/api/'.format(apicAddress=url)
    prepayload={
            "aaaUser": {
                "attributes": {
                    "name": "{user}".format(user=username), 
                    "pwd": "{passwd}".format(passwd=password)}
                }
            }
    headers = {
        'Content-Type': 'application/json'
        }
    payload = json.dumps(prepayload)

    login_url = base_url + 'aaaLogin.json'
    try:
        response = requests.request(
                "POST", 
                login_url, 
                headers=headers, 
                data=payload, 
                timeout=2, 
                verify=False)

        data = json.loads(response.text)
        token = {}
        token['APIC-Cookie'] = data["imdata"][0]['aaaLogin']['attributes']['token']

        #print(json.dumps(data, indent=4, sort_keys=True))
        return token
    except:
        print('Error occured')
    
if __name__ == '__main__':
    url = 'sandboxapicdc.cisco.com'
    username = 'admin'
    password = 'ciscopsdt'
    cookie = login(url,username,password)
    print(cookie)