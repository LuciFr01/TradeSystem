import socket
import requests
import json
from getmac import get_mac_address
public_ip = requests.get("https://ifconfig.me").text.strip()
local_ip = socket.gethostbyname(socket.gethostname())
mac_address = get_mac_address()

common_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "X-UserType": "USER",
    "X-SourceID": "WEB",
    "X-ClientLocalIP": local_ip,
    "X-ClientPublicIP": public_ip,
    "X-MACAddress": mac_address,
    "X-PrivateKey": "AVWsckWM"
}

def get_headers(exclude_keys=None, extra_headers=None):
    headers = common_header.copy()  
    if exclude_keys:
        for key in exclude_keys:
            headers.pop(key, None)
    if extra_headers:
        headers.update(extra_headers) 
    return headers  