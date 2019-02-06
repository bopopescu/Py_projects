import datetime, os
import shutil
print(datetime.date.today())
print(datetime.datetime.now())
#2019-01-31 14:35:20.771625
test_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S" )
test_time_list = test_time.split()
print(test_time_list)

print(os.getcwd())
print(os.listdir())

shutil.copytree("", ".\\")
