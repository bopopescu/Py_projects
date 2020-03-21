# print(input("what is your name"))


name = input("your name : ")
print(f"name is {name}")
import csv

with open('data.csv','a+') as data_file:
    writer = csv.writer(data_file)

    writer.writerow()