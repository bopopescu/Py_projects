import json
from pprint import pprint

with open('write_dut.json') as data_file:
    #data_item = json.loads(data_file.read())
    data_item = json.load(data_file)
#pprint(data_item)

print("*"*10)

"""
data =[]
with open('conn_str.json') as infile:
    for line in infile:
        data.append(json.loads(line))

for item in data:
    print(item)
    print("*"*4)
"""
#print(data_item['connection1']['DSN'])
#print(data_item['maps'][0]["id2"])
#print(data_item['parameters'][0]["id"])
#print(data['parameters'][0]["id"])

with open("write_dut.json","w") as outfile:
    json.dump(data_item, outfile, indent = 5)
               #ensure_ascii = False)