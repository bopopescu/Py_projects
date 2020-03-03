import json
from jsonpath import jsonpath
import jsonpath-ng
import requests
# Python	        JSON
# dict	            object
# list, tuple	    array
# str	            string
# int, long, float	number
# True	            true
# False	            false
# None	            null

# json_str = json.dumps(dict_type)
# json.dump(dict_type, file_write)
data_dict = {
  "name": "Ken",
  "age": 45,
  "married": True,
  "children": ("Alice","Bob"),
  "pets": ['Dog'],
  "cars": [
    {"model": "Audi A1", "mpg": 15.1},
    {"model": "Zeep Compass", "mpg": 18.1}
  ]
}
json_string = json.dumps(data_dict, indent=4, sort_keys=True)
print(json_string)
with open("json_str_write.json",  "w") as jsonWrite:
  json.dump(json_string, jsonWrite )
# print(data_dict)

# with open("json_data.json", 'w') as fin:
#     json.dump(data_dict, fin)


#
json_str = '{  "person":  { "name":  "Kenn",  "sex":  "male",  "age":  28}}'
# Decoding or converting JSON format in dictionary using loads()
dict_obj = json.loads(json_str)
print(dict_obj)
# check type of dict_obj
print("Type of dict_obj", type(dict_obj))
# get human object details
print("Person......",  dict_obj.get('person'))

#
with open("json_data.json", 'r') as fread:
  data_dict = json.load(fread)
print(data_dict)

#

# pythn_data = [1,2,3]
# json_data =  json.dumps(pythn_data)
# print(f"type of json_data: {type(json_data)}")   #  type of json_data: <class 'str'>

#
# Repeated key in JSON String
# RFC specifies the key name should be unique in a JSON object, but it's not mandatory.
# Python JSON library does not raise an exception of repeated objects in JSON.
# It ignores all repeated key-value pair and considers only last key-value pair among them.
repeat_pair = '{"a":  1, "a":  2, "a":  3}'
json.loads(repeat_pair)
# {'a': 3}

#
import simplejson as json
with open('json_data.json', 'r') as f:
    json_text = f.read()


# Decode the JSON string into a Python dictionary.
apod_dict = json.loads(json_text)
print(apod_dict['name'])

# Encode the Python dictionary into a JSON string.
new_json_string = json.dumps(apod_dict, indent=4)
print(new_json_string)

# request_data = json_text.json() #  incorrect


with open("json_data.json",'r') as fread:
  dict_temp = json.load(fread)
print(jsonpath(dict_temp, "age"))