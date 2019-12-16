import json, requests, jsonpath

# post
url = "https://httpbin.org/get"
headerdata = {"name": "BRCM-4389", "email":"qa@litepoint.com", "number":"408-880-9080", "Content-Type": "applications/json"}
response = requests.get(url, headers=headerdata)
print(response.text)
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Type": "applications/json",
#     "Email": "qa@litepoint.com",
#     "Host": "httpbin.org",
#     "Name": "BRCM-4389",
#     "Number": "408-880-9080",
#     "User-Agent": "python-requests/2.21.0"
#   },
#   "origin": "173.139.55.94, 173.139.55.94",
#   "url": "https://httpbin.org/get"
# }
print(response.headers)
# {'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Origin': '*', 'Content-Encoding': 'gzip', 'Content-Type': 'application/json', 'Date': 'Thu, 12 Dec 20