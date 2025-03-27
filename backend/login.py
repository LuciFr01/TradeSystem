import http.client
import json
import ssl
import certifi
from headers import get_headers
from payloads import get_payload
from token_manager import save_tokens

def login():
    headers = get_headers()
    payload = json.dumps(get_payload()).encode("utf-8")

    context = ssl.create_default_context(cafile=certifi.where())
    conn = http.client.HTTPSConnection("apiconnect.angelone.in", context=context)

    conn.request("POST", "/rest/auth/angelbroking/user/v1/loginByPassword", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    if data.get("status"):
        tokens = data.get("data", {})
        save_tokens(tokens)
        print("Login successful!")
    else:
        print("Login failed:", data.get("message"))

if __name__ == "__main__":
    login()
