import json, requests, jsonpath

# response.text  # <class 'str'>  , json string
# response.headers is type <class 'requests.structures.CaseInsensitiveDict'>
# type of response.json() is <class 'dict'>

# text_dict =  json.loads(response.text)
# type of text_dict is <class 'dict'>

# Get
# response = requests.get(url, headers=headerdata)
url = "https://httpbin.org/get"

headerdata = {"name": "BRCM-4389", "email":"qa@litepoint.com", "Cache-Control": "public", \
              "Content-Type": "applications/json"}
response = requests.get(url, headers=headerdata)
text =  response.text  # <class 'str'>
print(type(text))
print(text)
text_dict =  json.loads(text)
print(f"type of text_dict is {type(text_dict)}")
# type of text_dict is <class 'dict'>
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
print(f"type of response.headers is {type(response.headers)}")
print(response.headers)
# ('Date', 'Fri, 24 Jan 2020 06:02:54 GMT')
# ('Content-Type', 'application/json')
# ('Content-Length', '438')
# ('Connection', 'keep-alive')
# ('Server', 'gunicorn/19.9.0')
# ('Access-Control-Allow-Origin', '*')
# ('Access-Control-Allow-Credentials', 'true')

print(f"type of response.json() is {type(response.json())}")
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


response1 = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

print(f"headers is {response1.headers}")
# headers is {'Date': 'Tue, 25 Feb 2020 00:37:13 GMT',
# 'Content-Type': 'application/json; charset=utf-8',
# 'Transfer-Encoding': 'chunked',
# 'Server': 'GitHub.com',
# 'Status': '200 OK',
# 'X-RateLimit-Limit': '10',
# 'X-RateLimit-Remaining': '9',
# 'X-RateLimit-Reset': '1582591093',
# 'Cache-Control': 'no-cache',
# 'X-GitHub-Media-Type': 'github.v3;
# format=json',
# 'Link': '<https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython&page=2>;
# rel="next", <https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython&page=34>;
# rel="last"',
# 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type',
# 'Access-Control-Allow-Origin': '*',
# 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload',
# 'X-Frame-Options': 'deny',
# 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin',
# 'Content-Security-Policy': "default-src 'none'",
# 'Vary': 'Accept-Encoding, Accept, X-Requested-With',
# 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': '82D7:2E95:AC389:CC644:5E546C38'}

print(response1.json())
print("+++++++++++++++++++++++++++++++")
print(response1.request.url)
print(response.request.headers)
# {'User-Agent': 'python-requests/2.22.0',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept': '*/*',
# 'Connection': 'keep-alive',
# 'name': 'BRCM-4389',
# 'email': 'qa@litepoint.com',
# 'Cache-Control': 'public',
# 'Content-Type': 'applications/json'}
#
print("************************")
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
print(response.headers)