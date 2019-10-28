# chr vs ord
# str vs int

a = 'ab'
print(chr(1)) # not working, 1 is not a valid int for a char.
print(type(chr(1)) # not working

print(ord('a')) # 97
print(chr(97))  # a

# str works on primitive
ab = 100
c = str(100) # str(int), turns an int to a string
print(type(c), " and ", c) # <class 'str'>  and  100

# int(string) ==> int of base 10
# int(binary_string, base) == > int of base 10
c = "100"
cc = int(c)  
print("type of cc is {} and cc is {}".format(type(cc), cc))
# type of cc is <class 'int'> and cc is 100

binaryString="101"
int(binaryString, 2) # 5
int(binaryString, 8) # 65
#
    In[1]: float_num=128.8

    In[2]: int(float_num)
    Out[2]: 128

    In[3]: int("128.8")
    - --------------------------------------------------------------------------
    ValueError                                Traceback(most recent call last)
    < ipython-input-3-b36fcc5f3bf6 > in < module >
    --- -> 1 int("128.8")

    ValueError: invalid literal for int() with base 10: '128.8'
    #_________________________________________________________
    In[7]: str(128.8)
    Out[7]: '128.8'

    In[8]: float_str=str(128.8)

    In[9]: float(float_str)
    Out[9]: 128.8

    In[4]: float(128)
    Out[4]: 128.0

    In[5]: 5/2
    Out[5]: 2.5

    In[6]: 5//2
    Out[6]: 2
#_________________________________________
raw = r'this\t\n and that'
print(raw)  # this\t\n and that
# string operation
multi = """It was the best of times.
It was the worst of times."""

#____________________________________________________________________________
st = "Hope You Find It"
stt = st.lower() # convert the whole string to lower case
print(stt) #hope you find it
sttt = stt.upper() # convert the whole string to upper case
print(sttt) #HOPE YOU FIND IT
#
# reverse a string
myString = '1234567890'
print(myString[::-1]) #0987654321

# s is a string, 
s.lower(),s.upper(), s.islower(), s.isupper(): ignore non-alphabetic chars
s.lower()
s.upper() 
# -- returns the lowercase or uppercase version of the whole string
#s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
#s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string

s.islower()
s.isupper()
#_____________________________________________________________________________

s.count(substr, start, end)
# Does not count overlapping substrings.
    In[10]: cnt_count='foooo'

    In[11]: cnt_count.count('oo')
    Out[11]: 2

    In[12]: cnt_count.count('o', 1)
    Out[12]: 4

    In[13]: cnt_count.count('o')
    Out[13]: 4
    In[14]: cnt_count.count('a')
    Out[14]: 0
# ____________________________________________________________________

 


#____________________________________________________________________
s.find(substr, start, end)
    # search substr in range[start_pos, end_pos), excluding end_pos
    # returns the first index where it begins or -1 if not found
s.rfind(substr, start, end)

    In[16]: ss='foo goo foo goo'

    In[17]: ss.find(foo)
    Out[17]: -1

    In[18]: ss.find('foo')
    Out[18]: 0

    In[19]: ss.rfind('foo')
    Out[19]: 8

    In[20]: ss.rfind('foo', 5)
    Out[20]: 8

#____________________________________________________________________
s.isalnum()

s.isalpha()

s.isdigit()

s.isspace()

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
 print (isfloat('112.5'))
#____________________________________________________________________
s.lstrip(chars)
# Trims leading chars
    In[22]: "   foo goo   ".lstrip()
    Out[22]: 'foo goo   '

    In[24]: "foogaoo hpp jkk ".lstrip("foa")
    Out[24]: 'gaoo hpp jkk '

    In[25]: "foogaoo hpp jkk ".lstrip("afgo")
    Out[25]: ' hpp jkk '

    In[26]: "foogaoo hpp jkk ".lstrip("afgo ")
    Out[26]: 'hpp jkk '

    In[28]: 'http://www.realpython.com'.lstrip('/:pth').lstrip('/:pth')
    Out[28]: 'www.realpython.com'
#____________________________________________________________________
s.rstrip(chars)
# trims trailing chars
    In[29]: "   foo goo   ".rstrip(" o")
    Out[29]: '   foo g'
#____________________________________________________________________
s.strip(chars)

#____________________________________________________________________
s.split(sep=None, maxsplit=-1) # return a list
#  -- returns a list of substrings separated by the delimiter.
 ##   it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc'].
 #   As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
 #  return a list of one element if no delim found in the string

word = "\nthis is first page\nthis is 2nd page\nthis is third page\n"
word.split("\n") #['', 'this is first page', 'this is 2nd page', 'this is third page', '']
word.splitlines()#['', 'this is first page', 'this is 2nd page', 'this is third page']

word1 = "    1  2  3  "
word1.split()  # ['1', '2', '3']
word2=" \n   1 \n 2  3 \n"
word2.split()  # ['1', '2', '3']
word2.split('\n')  # [' ', '   1 ', ' 2  3 ', '']

word3="this, is,a,book, "
word3.split(',')
['this', ' is', 'a', 'book', ' ']

word4="this, is,a,book,"
word4.split(',')
['this', ' is', 'a', 'book', '']

word4.split(',', maxsplit=2)
['this', ' is', 'a,book,']

word4.split(',', maxsplit=3)
['this', ' is', 'a', 'book,']

word4.split('8')
['this, is,a,book,']

ss = "aba"
s = ss.split('a')
print(s, len(s))
# ['', 'b', ''] 3

#_______________________________________________________________
s.partition(< sep > )

Divides a string based on a separator.

s.partition( < sep > ) splits s at the first occurrence of string < sep > . The return value is a three-part tuple consisting of:

The portion of s preceding < sep >
< sep > itself
The portion of s following < sep >

'foo.bar'.partition('.')
('foo', '.', 'bar')

'foo.bar'.partition('..')
('foo.bar', '', '')

#_______________________________________________________________
s.join( < iterable > )
iterable must ba an iterable of strings
Concatenates strings from an iterable, returns a string

#joins a list of strings with s
# '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
s = ','
pp=s.join(["catch", "a", "cold"])  # 'catch,a,cold'

'---'.join(['foo', 23, 'bar'])
--- -> 1 '---'.join(['foo', 23, 'bar'])
TypeError: sequence item 1: expected str instance, int found
#_______________________________________________________________
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



    #____________________________________________________________________
    s.replace('old', 'new')
    #  -- returns a string where all occurrences of 'old' have been replaced by 'new'
    # if "old" is not found, no replacement happens


    #  -- returns a string with whitespace at the start and end removed.
    #____________________________________________________________________


ss = 'abc'
rst = ss.split()

print(f"split of '{ss}', type {type(rst)}, {len(rst)}, {rst}  ")
# split of 'a', type <class 'list'>, 2, ['', '']
# rst = ss.split('aa')
# split of 'a', type <class 'list'>, 1, ['a']
# ss = 'aaaa'
# split of 'aaaa', type <class 'list'>, 5, ['', '', '', '', '']
# ss = 'aaaa'
# rst = ss.split('aa')
# split of 'aaaa', type <class 'list'>, 3, ['', '', '']

# ss = ''
# # rst = ss.split()
# # split of '', type <class 'list'>, 0, []

# ss = ' '
# rst = ss.split(' ')
# split of ' ', type <class 'list'>, 2, ['', '']

# ss = ' a   b   c \n '
# rst = ss.split()
# split of ' a   b   c
#  ', type <class 'list'>, 3, ['a', 'b', 'c']

# ss = ' '
# rst = ss.split()
# split of ' ', type <class 'list'>, 0, []