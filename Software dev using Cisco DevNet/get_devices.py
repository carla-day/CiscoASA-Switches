import requests
from auth_token import get_token

def main():
    api_path = "https://sandboxdnac.cisco/dna"
    headers = {"content-type":"application/json", "X-Auth-Token": get_token()}
    
    get_resp = requests.get(
            f"{api_path}/intent/api/v1/network-device", 
            headers=headers, 
            verify=False)
    # get the devices id and ip addresss
    devices = []
    if get_resp.ok:
        for device in get_resp.json()['response']:
            device.append(f"{'Name: ' + device['id'], 'IP: '+ device['managementIpAddress']}")
            print(f"Id: {device['id']}") 
            print(f"IP: {device['managementIpAddress']}")

    get_resp.close()
    return devices
if __name__ == "__main__":
    main()
