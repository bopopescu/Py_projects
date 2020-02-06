import requests
#
# url = "https://api.github.com/search/repositories"
# params = {'q': 'requests+language:python'}
# headers = {'Accept': 'application/vnd.githubb.v3.text-match+json'}
# # res =  requests.get(url, params, headers,) # Not working
# # res =  requests.get(url )
# # print(f"status_code is {res.status_code}")
# query = {'q': 'requests+language:python'}
# header_data = {'Accept': 'application/vnd.github.v3.text-match+json'}
# response1 = requests.get(
#     'https://api.github.com/search/repositories',
#     params=query,
#     headers=header_data
# )
# # print(f"response1.status_code is {response1.status_code}")
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
#     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
# )
# # print(f"response.status_code  is {response.status_code}")
#
# # post
# data_body = {'key':'value'}
# url = "https://httpbin.org/post"
# res_post = requests.post(url, data=data_body)
# print(f"res_post.status_code is {res_post.status_code}")
#
# res_put = requests.put("https://httpbin.org/put", data=data_body)
# print(f"res_put is {res_put.status_code}")
#
# res_delete = requests.delete("https://httpbin.org/delete")
# print(f"res_delete is {res_delete.status_code}")
#
# # authentication
# res_auth = requests.get(url, auth=(username, passwd), timeout=1)
# res_token_auth = requests.get(url, auth=TokenAuth("123-token"))
#
# # response
# res_post.json()

# #
# url = "https://httpbin.org/get"
# headerdata = {"name": "BRCM-4389", "email":"qa@litepoint.com", "number":"408-880-9080", "Content-Type": "applications/json"}
# response = requests.get(url, headers=headerdata)
# # print(response.json())
# # print(response.headers)
#
# # for key, value in response.json().items():
# #     print(key, value)
#
# print(response.request)
#
# with open("src1.json","r") as fin:
#     json_obj = fin.read()
#     data_json = json.loads(json_obj)
#     response = requests.post(url, data=data_json)
# #
# I / P: AABBBCCCCAAA
# AABBC
# O / P: A2B3C4A3
# n = 5
#
#
# def test(word):
#     rst = ""
#     n = len(word)
#     if not word:
#         return rst
#     i = 0
#     cnt = 1
#     while i < n:
#         if i < n - 1:
#             if word[i] == word[i + 1]:
#                 cnt += 1
#
#             else:
#                 rst += (word[i] + str(cnt))
#                 cnt = 1
#             i += 1
#         elif i == n - 1:
#             rst += (word[i] + str(cnt))
#             break
#
#     return rst


# I / P: AABBBCCCCAAA
# AABBC
# O / P: A2B3C4A3
# n = 5
word = ['abcddcdddfHHHd', "AABBBCCCCAAA", "aAABBC",  "A", "a", "BB","acc","aacddeffgg"]



def test(word):
    rst = ""
    n = len(word)
    if not word:
        return rst
    i = 0
    cnt = 1
    while i < n:
        if i < n - 1:
            if word[i] == word[i + 1]:
                cnt += 1

            else:
                rst += (word[i] + str(cnt))
                cnt = 1
            i += 1
        elif i == n - 1:
            rst += (word[i] + str(cnt))
            break

    return rst

for wd in word:
    print(test(wd))