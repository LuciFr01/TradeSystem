import http.client
import json
from headers import get_headers
from payloads import get_payload 

headers = get_headers()

json_payload = json.dumps(get_payload())
payload = json_payload.encode("utf-8")

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
conn.request("POST", "/rest/auth/angelbroking/user/v1/loginByPassword", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
