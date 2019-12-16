import os
import time
import subprocess
import shutil
import datetime

# pytest
# skip test: -m, -v, -k

# @pytest.mark.skip

# run selected testes @mark
# pytest -k 

# group tests
# @pytest.mark.Group_name
#pytest -m Group_name

# run except test
# pytest -m "not Group_name"
 
# execute setup b4 or after each test.
# @pytest.fixture(scope="module")
# def setup()
#     global driver
#     driver = webdriver.Chrome()
# Everything after yield executed after test is done 
    #   yield
    #   driver.close()

# def test_reg(setup):
#     pass

##________________________________##






import zipfile
from collections import Counter
cnt_dict = {'a':4, 'b':8, 'c':10, 'd':4, 'e':10, 'f':5, 'h':5, 'g':5}
chr_key  = cnt_dict.keys()
# print(next(chr_key))
# Traceback (most recent call last):
#   File "C:/Users/jsun/Documents/Py_projects/log_test.py", line 10, in <module>
#     print(next(chr_key))
# TypeError: 'dict_keys' object is not an iterator
key_iter = iter(chr_key)
print(next(key_iter)) # 'a'

import copy
S = 'abc'
shifts = [3,5,9]

# tmp = shifts[:]
tmp = copy.copy(shifts)
tmp[0] = 100
print(shifts)
print("****")

def shiftingLetters(S, shifts) -> str:
    rst = ""
    if len(S) < len(shifts):
        shifts = shifts[:len(S)]
    tmp_lst = shifts[:]
    tmp_lst[0] = 0
    print(f'shifts is {shifts}')

    for i in range(1, len(tmp_lst)):
        tmp_lst[i] = tmp_lst[i - 1] + shifts[i - 1]

    print(f'shifts is {shifts}')
    total = sum(shifts)
    print(f"total  is {total}")
    for i in range(len(tmp_lst)):
        tmp_lst[i] = total - tmp_lst[i]
        num = tmp_lst[i] + ord(S[i])
        if num <= ord('z'):
            rst += chr(num)
        else:
            num = (num - ord('z')) % 26
            rst += chr(ord('a') + num)

    if len(S) > len(shifts):
        rst += S[len(shifts):]

    return rst








##
# ————————————————

##

##
# install package
def install_pkg(package_loc, package_p_drive, package_name):
    # copy package fitime_strList
    package_to_copy = os.path.join(package_p_drive, package_name)
    shutil.copy2(package_to_copy, package_loc)

    for zip_file in os.listdir(package_loc):
        zip_file = os.path.join(package_loc, zip_file)
        try:
            with zipfile.ZipFile(zip_file, "r") as file:
                file.extractall(package_loc)
                setup_exe = os.path.join(package_loc, "IQfact_plus", "setup.exe")
                while True:
                    if os.path.isfile(setup_exe):
                        break
                    else:
                        time.sleep(1)
                install_pkg = subprocess.Popen([setup_exe, "/S"])
                install_pkg.wait()

        except zipfile.BadZipFile:
            print("Error: Zipfile is corrupted.")

    # clean up zip folder
    for files in os.listdir(package_loc):
        file_to_delete = os.path.join(package_loc, files)
        if os.path.isfile(file_to_delete):
            os.remove(file_to_delete)
        else:
            shutil.rmtree(file_to_delete)
# _________________________________________

# copy test flows to bin

def copy_flows(run_dir, flow_to_test, flowfile_loc, setupfile_loc):
    for flow_name in os.listdir(flowfile_loc):
        # flow_name = os.path.split(flow_name)[-1]
        flow_name = flow_name.split("\\")[-1]
        src = os.path.join(flowfile_loc, flow_name)
        shutil.copy2(src, run_dir)
        flow_to_test.append(flow_name)
    for setup_file in os.listdir(setupfile_loc):
        src = os.path.join(setupfile_loc, setup_file)
        shutil.copy2(src, run_dir)
print("start")

#*****
# 1170 , 8/29
# 9/25
# 10_23
# 12_9

###
import json, requests, jsonpath
odices='{"k1":1, "k2":2}'
rst = json.loads(odices)
# print(type(rst)) # <class 'dict'>
# print(rst['k2']) # 2
#

# API with parameters.
#1.
url = "https://reqres.in/api/users?page=2"
response_1 = requests.get(url)
# print(type(response_1), response_1, sep=" --> ")
# <class 'requests.models.Response'> --> <Response [200]>

content  = response_1.content
# print(type(content))  # <class 'bytes'>
# print(content)
# b'{"page":2,"per_page":6}'

#
header = response_1.headers
print(type(header), header, sep=" --> ")
# <class 'requests.structures.CaseInsensitiveDict'> -->
{'Date': 'Wed, 11 Dec 2019 23:17:35 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=df6e47f7f298a5764dd4c33fdc28683151576106255; expires=Fri, 10-Jan-20 23:17:35 GMT; path=/; domain=.reqres.in; HttpOnly; Secure', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Etag': 'W/"414-k36Lu9tCb0XMJeh2/UG19C4xbw4"', 'Via': '1.1 vegur', 'Cache-Control': 'max-age=14400', 'CF-Cache-Status': 'HIT', 'Age': '4275', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Vary': 'Accept-Encoding', 'Server': 'cloudflare', 'CF-RAY': '543b2c406a1eed7f-SJC', 'Content-Encoding': 'gzip'}
# print(header["Date"])
# Wed, 11 Dec 2019 23:19:08 GMT
#
json_content = response_1.json
# print(type(json_content), json_content, sep="  -->  \n")
# <class 'method'>  -->
# <bound method Response.json of <Response [200]>>

# Convert to Json format
json_response = json.loads(response_1.text)
# print(type(json_response), json_response, sep=" -->  \n")
# <class 'dict'> -->
# {'page': 2, 'per_page': 6, 'total': 12, 'total_pages': 2, 'data': [{'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg'}, {'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/araa3185/128.jpg'}, {'id': 9, 'email': 'tobias.funke@reqres.in', 'first_name': 'Tobias', 'last_name': 'Funke', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg'}, {'id': 10, 'email': 'byron.fields@reqres.in', 'first_name': 'Byron', 'last_name': 'Fields', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg'}, {'id': 11, 'email': 'george.edwards@reqres.in', 'first_name': 'George', 'last_name': 'Edwards', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg'}, {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg'}]}

response_text = response_1.text
# print(type(response_text), response_text, sep="   --> \n")
# <class 'str'>   -->
# {"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/araa3185/128.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg"}]}

#
{
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/follettkyle/128.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/araa3185/128.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/russoedu/128.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/mrmoiree/128.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://s3.amazonaws.com/uifaces/faces/twitter/hebertialmeida/128.jpg"
        }
    ]
}
pages = jsonpath.jsonpath(json_response, "total_pages")
# print(type(pages), pages[0], sep=" --> \n")
# print(type(pages), pages, sep=" --> \n")
# <class 'list'> -->
# 2
# <class 'list'> -->
# [2]

data  = jsonpath.jsonpath(json_response, "data")
# print(len(data), data[0][2], sep="  --> \n")
# 1  -->
# {'id': 9, 'email': 'tobias.funke@reqres.in', 'first_name': 'Tobias', 'last_name': 'Funke', 'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/vivekprvr/128.jpg'}
# print(len(data[0]))
# for i in data[0]:
#     print(i["first_name"], end=", ")
# print()
# Michael, Lindsay, Tobias, Byron, George, Rachel,

data1 = data  = jsonpath.jsonpath(json_response, "data[0].first_name")
print(data1[0]) # Michael


#
status = response_1.status_code
# print(type(status), status, sep="  -->  \n")
# <class 'int'>  -->
# 200
# assert status == 201
#     assert status == 201
# AssertionError
#
# response_1.
# print(response_1.headers.get("Date"))
# Wed, 11 Dec 2019 23:39:53 GMT

# print(response_1.cookies)
# <RequestsCookieJar[<Cookie __cfduid=da79160fddc3496b271e2d8d789be04551576107652 for .reqres.in/>]>

# print(response_1.elapsed)
# 0:00:00.096220














##
import math
print(int(math.log2(8)) == math.log2(8) )
#_____________________________________________________________
#_______________________________________________________________
import os
cur_dir = os.path.abspath(__file__)
# print(cur_dir)
bb= os.path.dirname(cur_dir)
# print(os.path.dirname(cur_dir))
cc = os.path.dirname(bb)
# print(cc)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sss = [""]
# print("".join(sss))


