url = "mkyong.com#100#2015-10-1"
data = url.split("#")
print ("len is {}".format(len(data)))# len is 3
print(data) #['mkyong.com', '100', '2015-10-1']

#Split by first two white spaces only
alphabet = "a b c d e f g"
data = alphabet.split(" ",2) #maxsplit
print(data) #['a', 'b', 'c d e f g']

import socket
addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')
print(addr1, addr2)   # 216.58.195.78 98.138.252.38

mystring = 'zzzzzzabczzzzzzdefzzzzzzzzzghizzzzzzzzzzzz'
import re
mylist = re.split("[a-m]+",mystring)
print (mylist)
['zzzzzz', 'zzzzzz', 'zzzzzzzzz', 'zzzzzzzzzzzz']