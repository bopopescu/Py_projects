import json, requests, jsonpath

# post
url = "https://httpbin.org/get"
param = {"name": "BRCM-4389", "email":"qa@litepoint.com", "number":"408-880-9080", "Content-Type": "applications/json"}
response = requests.get(url, params=param)
print(response.text)
print(response.headers)


#   "args": {
#     "email": "qa@litepoint.com",
#     "name": "BRCM-4389",
#     "number": "408-880-9080"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.21.0"
#   },
#   "origin": "173.139.55.94, 173.139.55.94",
#   "url": "https://httpbin.org/get?name=BRCM-4389&email=qa%40litepoint.com&number=408-880-9080"
# }




