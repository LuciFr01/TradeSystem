import http.client
import json
from headers import get_headers
import pandas as pd
from token_manager import load_tokens


def fetch_market_data(payload):
    tokens = load_tokens()
    auth_token = tokens.get("jwtToken")

    if not auth_token:
        print("Error: No authToken found in tokens.json. Please log in again.")
        return

    conn = http.client.HTTPSConnection("apiconnect.angelone.in")
    headers = get_headers(extra_headers={'Authorization': f'Bearer {auth_token}'})
    
    conn.request("POST", "/rest/secure/angelbroking/market/v1/quote/", json.dumps(payload), headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    print(json.dumps(data, indent=4))

    if not data.get("status"):
        print(f"Error: {data.get('message')}")
        return None

    market_data = data.get("data", {}).get("fetched", [])
    if not market_data:
        print("No market data fetched.")
        return None

    df = pd.DataFrame(market_data)
    df = df[['tradingSymbol', 'ltp', 'open', 'high', 'low', 'close']]
    return df

if __name__ == "__main__":
    user_input = input("Enter JSON payload: ")
    try:
        payload = json.loads(user_input)
        df = fetch_market_data(payload)
        if df is not None:
            print(df)
    except json.JSONDecodeError:
        print("Invalid JSON input.")