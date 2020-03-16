import json, requests, jsonpath

# response.text  # <class 'str'>  , json string
# response.headers is type <class 'requests.structures.CaseInsensitiveDict'>
# response.json() is <class 'dict'>

# text_dict =  json.loads(response.text)
# type of text_dict is <class 'dict'>

# Get
# response = requests.get(url, headers=headerdata)
url = "https://httpbin.org/get"

headerdata = {"name": "BRCM-4389", "email":"qa@litepoint.com", "Cache-Control": "public", \
              "Content-Type": "applications/json"}
response = requests.get(url, headers=headerdata)

res_text = response.text
res_headers = response.headers
res_json = response.json()
res_content = response.content
res_status_code = response.status_code
res_request_headers  = response.request.headers

# print(f"{type(res_text)}")  # <class 'str'>
# print(f"{res_text}")
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Cache-Control": "public",
#     "Content-Type": "applications/json",
#     "Email": "qa@litepoint.com",
#     "Host": "httpbin.org",
#     "Name": "BRCM-4389",
#     "User-Agent": "python-requests/2.22.0",
#     "X-Amzn-Trace-Id": "Root=1-5e6ed078-56322add54976dcc502cc4f4"
#   },
#   "origin": "73.92.34.32",
#   "url": "https://httpbin.org/get"
# }

# print(f"{res_content}")
# b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Cache-Control": "public", \n    "Content-Type": "applications/json", \n    "Email": "qa@litepoint.com", \n    "Host": "httpbin.org", \n    "Name": "BRCM-4389", \n    "User-Agent": "python-requests/2.22.0", \n    "X-Amzn-Trace-Id": "Root=1-5e6eeb3b-9094b424d298a5603c5a8d84"\n  }, \n  "origin": "73.92.34.32", \n  "url": "https://httpbin.org/get"\n}\n'

# print(res_status_code)
# 200

# print(res_request_headers)
# {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive',
# 'name': 'BRCM-4389', 'email': 'qa@litepoint.com', 'Cache-Control': 'public', 'Content-Type': 'applications/json'}

# print(res_headers)
# {'Date': 'Mon, 16 Mar 2020 03:01:50 GMT', 'Content-Type': 'application/json', 'Content-Length': '439', 'Connection': 'keep-alive',
# 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}


# **********************************************************************
response1 = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
# print(response1.request.url)

import json, requests, jsonpath









