import csv

# my data rows as dictionary objects
test_1 = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

test_v = []
dict_1 = dict([("Tech", ["wifi", "wifi_mps", "AX_mps", "RSDB"])])
dict_4 = dict([("API", ["EVM", "TX_Power", "PER", "RX_Sens", "Mask",])])
dict_2 = dict([("Freq", [2412, 2437, 2482, 5180])])
dict_3 = dict([("Data_rate", [6, 9 , 48, 54, 216])])
dict_5 = dict([("RU", [0, 37, 53,61,65,67])])
for i in range(1,6):
    test_v.append("_".join(["dict", str(i)]))

# field names
fields = ['Tech', 'API', 'Freq', 'Data_rate', "RU"]
# name of csv file
filename = "dict_wifi.csv"

with open(filename, "w") as csvIn:
    csv_wr_dict = csv.DictWriter(csvIn, fieldnames=fields)
    csv_wr_dict.writerow(test_v)


