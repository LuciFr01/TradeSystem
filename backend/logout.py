import http.client
import json
import ssl
import certifi
from headers import get_headers
from token_manager import load_tokens, save_tokens
from payloads import get_payload  # Importing to fetch CLIENT_CODE

def logout():
    """Handles user logout by using stored tokens and clearing them."""
    tokens = load_tokens()
    if not tokens or "jwtToken" not in tokens:
        print("No active session found.")
        return

    # Fetch CLIENT_CODE from payloads.py
    client_code = get_payload().get("clientcode", "")
    if not client_code:
        print("CLIENT_CODE is missing in payloads.py.")
        return

    headers = get_headers(extra_headers={"Authorization": f"Bearer {tokens['jwtToken']}"})
    payload = json.dumps({"clientcode": client_code}).encode("utf-8")

    context = ssl.create_default_context(cafile=certifi.where())
    conn = http.client.HTTPSConnection("apiconnect.angelone.in", context=context)

    conn.request("POST", "/rest/secure/angelbroking/user/v1/logout", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    if data.get("status"):
        # Overwrite tokens.json with an empty object
        save_tokens({})
        print("Logout successful! Tokens cleared.")
    else:
        print("Logout failed:", data.get("message"))

if __name__ == "__main__":
    logout()
