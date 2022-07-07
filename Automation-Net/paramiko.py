import time
import paramiko
from getpass import *

#issue command and wait 1 sec for it to be processed
def send_cmd(conn, command):
    conn.send(command + "\n")
    time.sleep(1.0)
    

def get_output(conn):
    #read data and decode the byte string as UTF-8
    return conn.recv(65535).decode('utf-8')

def main():
    #execute
    #host dict, for script we can just import the host dict text file
    # on the script we want to mask each ip in the dict
    # i.e host_dict = open('samplelist.txt', 'r+') 
    #r+ lets you read and write.
    
    host_dict = {
        'R1': 'show running-config | section vrf_definition',
        'R2': 'show running-config vrf',
    }
    #here we are extracting key and value of each host in dict
    for hostname, vrf_cmd in host_dict.items():

        conn_params = paramiko.SSHClient()
        #dont let paramiko refuse connections if theres no SSH key
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #connection paramaeters
        conn_params.connect(
        hostname=hostname,
        port= 22,
        username= getuser("Type username"),
        password= getpass("Type password"),
        look_for_keys=False,
        allow_agent=False,
        )
        #get interactive shell + wait 1
        conn = conn_params.invoke_shell()
        time.sleep(1.0)
        print(f"Logged into {get_output(conn).strip()} successfully")
