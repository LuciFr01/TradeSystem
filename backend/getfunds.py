import http.client
import json
import ssl
import certifi
from headers import get_headers
from token_manager import load_tokens

def get_funds():
    """Fetches the user's available funds using stored authentication tokens."""
    tokens = load_tokens()
    if not tokens or "jwtToken" not in tokens:
        print("No active session found. Please log in first.")
        return

    headers = get_headers(extra_headers={"Authorization": f"Bearer {tokens['jwtToken']}"})
    payload = "".encode("utf-8")  # Empty payload for GET request

    context = ssl.create_default_context(cafile=certifi.where())
    conn = http.client.HTTPSConnection("apiconnect.angelone.in", context=context)

    conn.request("GET", "/rest/secure/angelbroking/user/v1/getRMS", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    if data.get("status"):
        print("Funds Data:", json.dumps(data, indent=2))
    else:
        print("Failed to fetch funds:", data.get("message"))

if __name__ == "__main__":
    get_funds()
