import json
from credentials import SECRET_KEY, Client_Code,Password
import pyotp

totp = pyotp.TOTP(SECRET_KEY)
TOTP_CODE = totp.now()
common_payload = {
    "clientcode": Client_Code,
    "password": Password,
    "totp": TOTP_CODE,
    "state": "STATE_VARIABLE"
}

def get_payload(exclude_keys=None, extra_payload=None):
    payload = common_payload.copy()  
    if exclude_keys:
        for key in exclude_keys:
            payload.pop(key, None) 
    if extra_payload:
        payload.update(extra_payload) 
    return payload