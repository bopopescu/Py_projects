pi = 3.14
# text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is ' + str(pi)  ## yes

raw = r'this\t\n and that'
print(raw)  # this\t\n and that
# string operation
multi = """It was the best of times.
It was the worst of times."""
st = "Hope You Find It"
stt = st.lower()
print(st)

myString = '1234567890'
print(myString[::-1]) #0987654321

#s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
#s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
#s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string

#s.find('other') -- searches given string,
#returns the first index where it begins or -1 if not found
#s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'

#s.strip() -- returns a string with whitespace at the start and end removed.
#s.split('delim') -- returns a list of substrings separated by the delimiter.
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