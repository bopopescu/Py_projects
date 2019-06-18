
import json
from pprint import pprint
data = [{
    'wifi': 0,
    'bt': 1,
    '11ac': "Legacy",
    '11ax': {
        '11abgnac': 4
    }
},
{
    '11ax': 0,
    '11ac': 1,
    '11abgn': "Legacy",
    '11ad': {
        '11abgnac': 4
    }
}
    ]

#print ("dic data is {}".format(data))
#pprint(data)

#{'wifi': 0, 'bt': 1, '11ac': 'Legacy', '11ax': {'11abgnac': 4}}
#print(len(data)) # 4

json_string = json.dumps(data)
print(type(json_string))#string
print(json_string)
#{"wifi": 0, "bt": 1, "11ac": "Legacy", "11ax": {"11abgnac": 4}}
json_list = json_string.split(",")
#print(json_list)
"""
for item in json_list:
    print(item)
"""
#print(len(json_string)) #63

#dic_data = json.loads(json_string)
#print(type(dic_data)) #dict


#new_str = json_string.split(',')
#['{"wifi":', '0,', '"bt":', '1,', '"11ac":', '"Legacy",', '"11ax":', '{"11abgnac":', '4}}']
#print(new_str)

with open("write_dut_1.json","w") as outfile:
    json.dump(data, outfile, indent=5)

with open("write_dut_1.json", "r") as infile:
    data_item = json.load(infile)
#print(data_item)
print(type(data_item))

#import pandas
#data_1 = pandas.read_json("write_dut_1.json", orient="columns")

while True:
    input1 = input("Enter a number: ")
    print(input1)
    if int(input1) > 10:
        break