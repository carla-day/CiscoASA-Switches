import requests
from requests.auth import HTTPBasicAuth
import getpass
def get_token(key):
    api_path = "https://sandboxdnac.cisco.com/dna"
    #auth = ("devnetuser", "Cisco123!")
    headers = {"content-type": "application/json"}
    #post request
    resp = requests.post(
            f"{api_path}/system/api/v1/auth/token", auth = HTTPBasicAuth(
                username='devnetuser', 
                password= key,
                ), 
                headers=headers, 
                verify=False)
    #print the token 
    resp.raise_for_status()
    token = resp.json()
    return token['Token']
def main():
    #test code
    password = getpass.getpass("Enter password ")
    token = get_token(password)
    print(token)

if __name__ == "__main__":
    main()
