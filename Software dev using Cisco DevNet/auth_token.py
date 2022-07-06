import requests
from requests.auth import HTTPBasicAuth
def get_token():
    api_path = "https://sandboxdnac.cisco.com/dna"
    #auth = ("devnetuser", "Cisco123!")
    headers = {"content-type": "application/json"}
    
    #post request
    resp = requests.post(
            f"{api_path}/system/api/v1/auth/token", auth = HTTPBasicAuth(
                username='devnetuser', 
                password='Cisco123!'
                ), 
                headers=headers, 
                verify=False)
    #print the token 
    resp.raise_for_status()
    token = resp.json()
    return token['Token']
def main():
    #test code
    token = get_token()
    print(token)

if __name__ == "__main__":
    main()
