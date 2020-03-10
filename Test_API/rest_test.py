import requests, json


url = 'https://api.github.com/search/repositories'
parameters = {'q': 'requests+language:python'}
headers={'Accept': 'application/vnd.github.v3.text-match+json'}

# get
response = requests.get(url, params=parameters, headers=headers)
res_dict = response.json()

res_text = response.text
jsonstr_to_dict = json.loads(res_text)

encodeing = (response.encoding)
response_headers = response.headers
url = response.url
res = response.status_code




# post
url = 'https://httpbin.org/post'
json_data = {'key':'value'}
response = requests.post(url, json=json_data)

req_url =     response.request.url
req_body =    response.request.body
req_headers = response.request.headers


##
response_post =  requests.post('https://httpbin.org/post',   data={'key':'value'})
response_put  =  requests.put('https://httpbin.org/put',     data={'key':'value'})
response_patch = requests.patch('https://httpbin.org/patch', data={'key':'value'})

response_delete = requests.delete('https://httpbin.org/delete')
response_head = requests.head('https://httpbin.org/get')
# print(response_head)  <Response [200]>
response_options =  requests.options('https://httpbin.org/get')


##
# Authentication

res_auth = requests.get('https://api.github.com/user', auth=("brb45", "zh" ), timeout=1)
# print(res_auth.status_code)
response = res_auth.json()
response_headers= response.headers

req_headers = response.request.headers


## Upload file
url = 'http://localhost:5000/upload'
with open('sid.jpg', 'rb') as f:

    files = {'image': f}

    r = requests.post(url, files=files)
    print(r.text)

url = "https:// ../analytics/upload_file"
headers = {'Username': 'abc@gmail.com', 'apikey':'123-456'}
with open("abc.zip","rb") as fin:
    files = {"file": ("abc.zip", fin)}
    response = requests.post(url, files=files, headers=headers)
file_id = response.json()['file_ids']

print()

