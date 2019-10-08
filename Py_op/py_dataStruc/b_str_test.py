# char vs int
# str vs int

a = 'ab'
print(chr(1)) # not working
print(type(chr(1)), chr(98)) # not working

print(ord('a')) # 97
print(chr(97))  # a


ab = 100
c = str(100)
print(type(c), " and ", c) # <class 'str'>  and  100

cc = int(c)
print("type of cc is {} and cc is {}".format(type(cc), cc))
# type of cc is <class 'int'> and cc is 100

#_________________________________________

pi = 3.14
# text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is ' + str(pi)  ## yes

raw = r'this\t\n and that'
print(raw)  # this\t\n and that
# string operation
multi = """It was the best of times.
It was the worst of times."""

#
st = "Hope You Find It"
stt = st.lower() # convert the whole string to lower case
print(stt) #hope you find it
sttt = stt.upper() # convert the whole string to upper case
print(sttt) #HOPE YOU FIND IT
#

myString = '1234567890'
print(myString[::-1]) #0987654321

s.lower()
s.upper() 
# -- returns the lowercase or uppercase version of the whole string
#s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
#s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string

s.find('other')
#  -- searches given string,
#returns the first index where it begins or -1 if not found
# s.find(substring, start_pos, end_pos) , search substr in range[start_pos, end_pos), excluding end_pos

s.replace('old', 'new')
#  -- returns a string where all occurrences of 'old' have been replaced by 'new'
# if "old" is not found, no replacement happens

s.strip()
#  -- returns a string with whitespace at the start and end removed.

s.split('delim')
#  -- returns a list of substrings separated by the delimiter.
 ##   it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc'].
 #   As a convenient special case s.split() (with no arguments) splits on all whitespace chars.

word = "\nthis is first page\nthis is 2nd page\nthis is third page\n"
word.split("\n") #['', 'this is first page', 'this is 2nd page', 'this is third page', '']
word.splitlines()#['', 'this is first page', 'this is 2nd page', 'this is third page']

s.join(list)
#joins a list of strings with s
# '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
s = ','
pp = s.join(["catch","a","cold"])

s[1:4] #is 'ell' #-- chars starting at index 1 and extending up to but not including index 4
s[1:] #is 'ello' #-- omitting either index defaults to the start or end of the string
s[:] #is 'Hello' -- omitting both always gives us a copy of the whole thing
    #(this is the pythonic way to copy a sequence like a string or list)
s[1:100] #is 'ello' -- an index that is too big is truncated down to the string length

s[-1] # 'o' -- last char (1st from the end)
s[-4] # 'e' -- 4th from the end
s[:-3] # 'He' -- going up to but not including the last 3 chars.
s[-3:] # 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

print("this is \x61 \ngood example")
print(r"this is \x61 \ngood example")
this is a
good example
this is \x61 \ngood example

t_str = "automation test"
t_enum = list(enumerate(t_str))
print(type(t_enum)) #<class 'list'>
print(t_enum) #[(0, 'a'), (1, 'u'), (2, 't'), (3, 'o'), (4, 'm'), (5, 'a'), (6, 't'), (7, 'i'), (8, 'o'), (9, 'n'), (10, ' '), (11

print(":".join("abc")) #a:b:c

str.isalnum()	String consists of only alphanumeric characters (no symbols)
str.isalpha()	String consists of only alphabetic characters (no symbols)
str.islower()	String’s alphabetic characters are all lower case
str.isnumeric()	String consists of only numeric characters
str.isspace()	String consists of only whitespace characters
str.istitle()	String is in title case
str.isupper()	String’s alphabetic characters are all upper case

# str.strip([set of chars])
string = '   xoxo love xoxo    '
# print("string is {}, len is {}".format(string, len(string)))
# string is    xoxo love xoxo    , len is 21

str1 = string.strip()
#removed 3 leading spaces and 4 trailing spaces
# print("str1 is {}, len is {}".format(str1, len(str1)))
# str1 is xoxo love xoxo, len is 14

str2= string.strip('xoxo')
# # Nothing is removed
print("str2 is {}, len is {}".format(str2, len(str2)))
# # str2 is    xoxo love xoxo    , len is 21

str3= string.strip(' xoxo')
# #
print("str3 is {}, len is {}".format(str3, len(str3)))
# # str3 is love, len is 4

data = "wiiwnter"
print(data.strip("iw")) #nter

data1 ="appointment"
print(data1.strip("pa"))  #ointment