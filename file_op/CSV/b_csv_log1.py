import csv
#
from pprint import pprint
file_name = "data_set2.csv"
with open(file_name, "r") as infile:
    csvReader = csv.reader(infile) #<type '_csv.reader'>
    #print(type(csvReader))
    #title_line = next(csvReader) # ['Test_ID', 'Val']
    content = []
    for row in csvReader:
        #print(type(row)) #list
        content.append(row)
    #print(content)
    pprint(content)
    print("Total no. of rows: {}".format(csvReader.line_num))
"""
[['Test_ID', 'Val', '', '', '', '', ''],
 ['1', '100', '100', '100', '100', '100', '100'],
 ['2', '200', '200', '200', '200', '200', '200'],
 ['3', '300', '300', '300', '300', '300', '300']]

"""