import json, requests, jsonpath

# convert json obj in str form to dict type
json_obj = '{"loc": null,"in_use": false}'
python_dict = json.loads(json_obj)
print(f"type(python_dict) is {type(python_dict)}")
for key, val in python_dict.items():
    print(f"{key}:{val}", end="\n")
# type(python_dict) is <class 'dict'>
# loc:None
# in_use:False


#@@ 1.
# json object is json string of dict


# response = requests.post(url, data_in_dict_type)


# response.headers --> dict type
# response.headers.get("Content-Length")

# response.text  --> json object
# json.loads(response.text)
# same as 
# response.json()

# response.status_code

# response.url

# response.content # binary stream

# response.cookies

# print(response.elapsed) 0:00:00.414485

# print(response.history) []

# response.request => <PreparedRequest [POST]>


# post
url = "https://reqres.in/api/users"

with open("src1.json", "r") as fin:
    json_input_str = fin.read()
    # print(f"type: {type(json_input_str)}\n  {json_input_str}")
    # type: <class 'str'>
    # {
    #     "name": "morpheus",
    #     "job": "leader"
    # }
    req_json = json.loads(json_input_str)
    # print(f"type: {type(req_json)}\n  {req_json}")
    # type: <class 'dict'>
    # {'name': 'morpheus', 'job': 'leader'}
    response = requests.post(url, req_json)
    # print(response.status_code) # 201
    # print(response.content)
    # b'{"name":"morpheus","job":"leader","id":"530","createdAt":"2019-12-12T19:41:32.341Z"}'

    ##
    content_len = response.headers.get("Content-Length")
    response_json = json.loads(response.text)
    # print(f"\nresponse_json from POST is {response_json}\n")
    # response_json
    # from POST is {'name': 'BRCM_4389', 'job': '11AX on MW-7G', 'id': '598', 'createdAt': '2019-12-12T22:09:57.259Z'}

    id = jsonpath.jsonpath(response_json, 'id')
    # print(f"id is {id[0]}")  # id is 716
    createdAt= jsonpath.jsonpath(response_json,"createdAt")
    # print(f"createdAt is {createdAt[0]}")  # createdAt is 2019-12-13T22:37:08.370Z

    ##
    # response_json = json.loads(response.text) vs response.json()
    # print(f"type(response.json()) is {type(response.json())}") 
    # type(response.json()) is <class 'dict'>
    # print(f"response.json() is {response.json()}")
    # response.json() is {'name': 'BRCM_4389', 'job': '11AX on MW-7G', 'id': '114',
    #                     'createdAt': '2019-12-13T22:40:24.318Z'}


    #@@ 2.
    # print(f"type(response.headers) is {type(response.headers)}")
    # print(f"response.headers is {response.headers}")

# type(response.headers) is <class 'requests.structures.CaseInsensitiveDict'>

# response.headers is 
# {'Date': 'Fri, 13 Dec 2019 22:43:13 GMT', 
# 'Content-Type': 'application/json; charset=utf-8',
# 'Content-Length': '92', 'Connection': 'keep-alive',
# 'Set-Cookie': '__cfduid=d2b79012297c85452f4a19c0033325b6f1576276992; 
# expires=Sun, 12-Jan-20 22:43:12 GMT;
# path=/; domain=.reqres.in; HttpOnly; Secure', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*',
# 'Etag': 'W/"5c-oOvvBcBfXq6YiarlvMAo3LaIL5Y"', 
# 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC',
# 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
# 'Server': 'cloudflare', 'CF-RAY': '544b74a58e156d22-SJC'
# }

# print(response.headers["Date"]) Fri, 13 Dec 2019 22:45:46 GMT

#@@ 3.
# print(f"type(response.text) is {type(response.text)}")  type(response.text) is <class 'str'>

# print(f"type(response) is {type(response)}") type(response) is <class 'requests.models.Response'>

# print(response.url)  https://reqres.in/api/users

# print(response.content) b'{"name":"BRCM_4389","job":"11AX on MW-7G","id":"256","createdAt":"2019-12-13T22:52:00.789Z"}'

# print(response.text) {"name":"BRCM_4389","job":"11AX on MW-7G","id":"434","createdAt":"2019-12-13T22:52:26.945Z"}

# print(response.status_code) 201

# print(response.cookies) <RequestsCookieJar[<Cookie __cfduid=df741ae771b55b848ed73c6f69f80d4401576277654 for .reqres.in/>]>

# print(response.elapsed) 0:00:00.414485

# print(response.history) []

# print(response.request) <PreparedRequest [POST]>
