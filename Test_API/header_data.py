import json, requests, jsonpath

# Get
# response = requests.get(url, headers=headerdata)
url = "https://httpbin.org/get"

headerdata = {"name": "BRCM-4389", "email":"qa@litepoint.com", "number":"408-880-9080", \
              "Content-Type": "applications/json"}
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


# ('Date', 'Fri, 24 Jan 2020 06:02:54 GMT')
# ('Content-Type', 'application/json')
# ('Content-Length', '438')
# ('Connection', 'keep-alive')
# ('Server', 'gunicorn/19.9.0')
# ('Access-Control-Allow-Origin', '*')
# ('Access-Control-Allow-Credentials', 'true')

for key, value in response.json().items():
    print(key, value)

# args {}
# headers {
# 'Accept': '*/*',
# 'Accept-Encoding': 'gzip, deflate',
# 'Content-Type': 'applications/json',
# 'Email': 'qa@litepoint.com',
#  'Host': 'httpbin.org',
#  'Name': 'BRCM-4389',
#  'Number': '408-880-9080',
#  'User-Agent': 'python-requests/2.22.0',
#  'X-Amzn-Trace-Id':
#  'Root=1-5e2a8977-ba4224299942c80d0a160dde'}


# origin 73.92.34.32
# url https: // httpbin.org/get
