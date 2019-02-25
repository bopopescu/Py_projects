"""

#open to read
import errno
import os
filepath = "C:/Users/jsun/Documents/pyProjects/Auto_Jenkins/test_case"
log_file = os.path.join(filepath,"doc_dir.txt")
try:
    with open(log_file,"w") as my_file:
        my_file.write("start of test")
except IOError as error:
    if error.errno == errno.ENOENT:
        print ('ignoring error because directory or file is not there')
    else:
        print("error to open\n")
#open to write
import os
import errno
if not os.path.exists(filepath):
    try:
        os.makedirs(filepath)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise
with open(log_file, 'w') as my_file:
    my_file.write("Start of the test\n")
"""
"""
import os.path
path = os.path.join("C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins","QA_Auto.py")

file_dir = os.path.split(path)

file_name = os.path.splitext(file_dir[1])

ls_dir = os.listdir("C:\\Users\\jsun\\Documents\\pyProjects\\Auto_Jenkins")
dir_name = os.path.dirname(path)
is_dir = os.path.isdir(dir_name)
try:
    with open("doc_dir.txt", "w") as fout:
        file_list =[]
        [file_list.append(f) for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]
        #fout.writelines(file_list)
        for item in file_list:
            fout.write(item+"\n")
except IOError:
    print("An I/O error has occurred!")
except:
    print("An unknown error has occurred!")
finally:
    print("file write done")

"""
"""
s = "Automation test results parsing starts: Jekins query and then set up the flag for testing. "
words = s.split()
print("words is ", words)
output = ""
for counter, element in enumerate(words):
    if(counter % 5 == 0):
        output += '\n'
    output +="{0:>10s}".format(element)
print (output)
print ("Test result {0:.3f} in floating".format(5.1234))
#left-align the number and center the string with width of 16
print("Test has {0:<4} errors in  {1:^16}!".format(5, "Error-4"))
print("Log contains {0:>4} errors in {1:*^16s}!".format(5, "Error_12"))

with open("log_rec.txt","w") as fout:
    fout.write(output)
"""
#list is mutable and is passed as a reference
def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)

outer_list = ['one', 'two', 'three']
print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)# outer_list has been changed by the function
"""
before, outer_list = ['one', 'two', 'three']
got ['one', 'two', 'three']
changed to ['one', 'two', 'three', 'four']
after, outer_list = ['one', 'two', 'three', 'four']
"""
#outer_list has not been changed
def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)

outer_list = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)
"""
before, outer_list = ['we', 'like', 'proper', 'English']
got ['we', 'like', 'proper', 'English']
set to ['and', 'we', 'can', 'not', 'lie']
after, outer_list = ['we', 'like', 'proper', 'English']
"""

#String - an immutable type
import os.path
fname = "fun2.py"
file_check = os.path.isfile(fname)

(filepath, filename) = os.path.split("c:\\music\\ap\\mahadeva.mp3")
#os.path.split returns a tuple
#('c:\\music\\ap', 'mahadeva.mp3')
file_path = (fname) #return a str
print(file_path)

file_alt_path = os.path.split(fname)
#('', 'fun2.py')
print(file_alt_path)
print(os.environ)
print(os.getenv(fname))

from pathlib import Path
my_file = Path(file_path)
#my_file = os.path.abspath(fname)
print (type(my_file))
print(my_file)
if not my_file.is_file():
    print ("it is not a directory")

filename = "file_name_test.py"
if not os.path.exists(filename):
    print(filename, "does not exist")
    #file(filename, 'w').close()
