import requests

#@@ 1.
# https://api.github.com/search/repositories?q=requests%2Blanguage%3Apython
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
# response.content -> raw bytes
# response.text   --> json string
# response.json()  --> python dict
# json.loads(response.text) --> python dict

# response.encoding = "utf-8"
# response.headers --> python dict
# response.url
# response1.request.url
# response.status_code
#
# print(response.request)
# <PreparedRequest [GET]>
# response.request.headers #dictionary
# response.request.headers["content-type"]  #  applications/json


response = requests.post('https://httpbin.org/post', json={'key':'value'})
# response.request.headers['Content-Type']
# 'application/json'
# response.request.url   # 'https://httpbin.org/post'

# response.request.body
# b'{"key": "value"}'
# for GET: response.request.body returns None

# pass by the bytes
requests.get(
     'https://api.github.com/search/repositories',
     params=b'q=requests+language:python',
 )

# customize headers
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# print(response.headers)
# for key in response.headers:
#     print(key)
# print(response.headers["Accept"])


## post
response_post = requests.post('https://httpbin.org/post', data={'key':'value'})
response_put  = requests.put('https://httpbin.org/put', data={'key':'value'})

response_delete = requests.delete('https://httpbin.org/delete')

response_head = requests.head('https://httpbin.org/get')
# print(response_head)  <Response [200]>

response_patch = requests.patch('https://httpbin.org/patch', data={'key':'value'})

response_options =  requests.options('https://httpbin.org/get')


# data takes dict, list of tuples, bytes, and file.
# payload is passed in the message body for post, put, and patch

# get: can pass data in query string-- params



# Authentication

from getpass import getpass
res_auth = requests.get('https://api.github.com/user', auth=("brb45","zh" ), timeout=1)
# res_auth = requests.get('https://api.github.com/user', auth=('username', getpass()))
# print(res_auth.status_code)

# from requests.auth import HTTPBasicAuth
# requests.get(
#      'https://api.github.com/user',
#      auth=HTTPBasicAuth('username', getpass())
#  )
# print(res_auth.status_code) # 200
# print(res_auth.url)    # https://api.github.com/user
# print(res_auth.encoding) # utf-8


import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))


#Passing Parameters In URLs
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url) # https://httpbin.org/get?key1=value1&key2=value2

##
# Binary Response Content
# You can also access the response body as bytes, for non-text requests:
#
# >>> r.content
# b'[{"repository":{"open_issues":0,"url":"https://github.com/...


##
# There’s also a builtin JSON decoder, in case you’re dealing with JSON data:
#
# >>> import requests
#
# >>> r = requests.get('https://api.github.com/events')
# >>> r.json()
# [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
#

##
# print(f"r.cookies is {r.cookies}")  r.cookies is <RequestsCookieJar[]>
# print(f"r.cookies is {r.cookies["cookie_name"]}")


#@@ Upload a file
#!/usr/bin/env python3

import requests as req

url = 'http://localhost:5000/upload'

with open('sid.jpg', 'rb') as f:

    files = {'image': f}

    r = req.post(url, files=files)
    print(r.text)

#@@ Streaming the data
#!/usr/bin/env python3

import requests as req

url = "https://docs.oracle.com/javase/specs/jls/se8/jls8.pdf"

local_filename = url.split('/')[-1]

r = req.get(url, stream=True)

with open(local_filename, 'wb') as f:

    for chunk in r.iter_content(chunk_size=1024):

        f.write(chunk)
#@@
