
# importing the csv module
import csv

# field names
fields = ["TECHNOLOGY", "FREQ_MHZ", "DATA_RATE*", "TEST*", "TX_POWER_DBM*", "ANTENNA"]

# data rows of csv file
rows1 = [['WIFI_MPS',     2422,   'DSSS-1',    'E,M,P',     15.0, (1,0,0,0)],
        [  ""      ,     2457,   'CCK_5-5',    'E,M,P,S',   ""      ,"" ],
        [   ""     ,     2484,   ""      ,    "L,H,S",      ""   , ""    ]
    ]
rows = [['WIFI_MPS',     2422,   'DSSS-1',    'E,M,P',     15.0, (1,0,0,0)],
        [            2457,   'CCK_5-5',    'E,M,P,S',   ""      ,"" ],
        [             2484,   ""      ,    "L,H,S",      ""   , ""    ]
    ]
# name of csv file
filename = "test_mps_flow.csv"


# writing to csv file
with open(filename, 'w') as csvfile:
    csvRwriter = csv.writer(csvfile)
    csvRwriter.writerow(fields)
    # writing the data rows
    csvRwriter.writerows(rows)
with open("mps_flow.csv","w") as csvfile_a:
    csv_write = csv.writer(csvfile_a)
    csv_write.writerow(fields)
    csv_write.writerows(rows)

with open("mps_flow.csv","r") as fin_in:
    for row in fin_in:
        print(row)