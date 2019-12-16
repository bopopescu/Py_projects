import requests, json, jsonpath
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth("br","zh"))
    print(json.loads(response.text))
    print(response.status_code)
test_with_authentication()

def test_oauth_api():
    token_url = "https://thetestingworldapi.com/Token"
    data= {"grant_type":"password", "username":"admin", "password":"passwd"}
    response = requests.post(token_url, data)

    token_value = jsonpath.jsonpath(response.json(), "access_token")

    auth = {"Authorization": "Bearer "+ token_value[0]}
    API_URL = "http://thetestingworldapi.com/api/StDetails/1104"
    response  = requests.get(API_URL, headers=auth)
