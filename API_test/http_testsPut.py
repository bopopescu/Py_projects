import json, requests, jsonpath

# post
url = "https://reqres.in/api/users/2"

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
    response = requests.put(url, req_json)
    # print(response.status_code) # 201
    # print(response.content)
    # b'{"name":"morpheus","job":"leader","id":"530","createdAt":"2019-12-12T19:41:32.341Z"}'

    ##
    content_len = response.headers.get("Content-Length")
    response_json = json.loads(response.text)
    print(f"response_json from PUT is \n {response_json}")
    # response_json
    # from PUT is   {'name': 'BRCM_4389', 'job': '11AX on MW-7G', 'updatedAt': '2019-12-12T22:11:14.094Z'}
    #
    # response_json
    # from POST is {'name': 'BRCM_4389', 'job': '11AX on MW-7G', 'id': '598', 'createdAt': '2019-12-12T22:09:57.259Z'}
    # id = jsonpath.jsonpath(response_json, 'id')
    # print(f"id is {id[0]}")  # id is 716
    # createdAt= jsonpath.jsonpath(response_json,"createdAt")
    # print(f"createdAt is {createdAt[0]}")
    name = jsonpath.jsonpath(response_json, "name")
    print(f"name is {name[0]}") # name is BRCM_4389
    ## put
    print(f"put status code is {response.status_code}") # 200
