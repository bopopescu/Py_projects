#read() return a string for the whole content
#read(n) return content of n bytes, upto 5555 bytes
#readlines(n): read in n bytes, return a list of strings upto n bytes, each string is a line ending with '\n'
#readline(n) is same as readlines() still read the whole thing


#"""
file_name = r'logging_test.txt'
# 2018-02-10 18: 33: 52, 527 - DEBUG - End
# 2018-02-10 18: 33: 52, 527 - INFO - The log
# 2018-02-10 18: 33: 52, 527 - WARNING - An
# 2018-02-10 18: 33: 52, 527 - ERROR - An err.


with open(file_name, 'r') as infile:
    text = infile.read().splitlines()  # a list of strings stripped of "\n"
    # print(text)
# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log',
#     '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']

with open(file_name, "r") as f:
    lines = f.readlines(120)  # 
    # print(f.tell())
    #print(type(lines)) # list of strings
    # print(lines)
    # ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n',
    #     '2018-02-10 18:33:52,527 - WARNING- An\n', '2018-02-10 18:33:52,527 - ERROR- An err.\n']


with open(file_name, 'r') as infile:
    text = infile.read(120)
    '2018-02-10 18: 33: 52, 527 - DEBUG - End\n2018-02-10 18: 33: 52, 527 - INFO - The log\n2018-02-10 18: 33: 52, 527 - WARNING - An\n2018-'
# 2018-02-10 18: 33: 52, 527 - DEBUG - End
# 2018-02-10 18: 33: 52, 527 - INFO - The log
# 2018-02-10 18: 33: 52, 527 - WARNING - An
# 2018-


def read_line_by_line():
    with open(file_name, "r") as f:
        line = f.readline()
        lines = []
        while line:
            #print(f.tell())
            lines.append(line)
            line = f.readline()
        print(lines)


# read_line_by_line()
# ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n',
#     '2018-02-10 18:33:52,527 - WARNING- An\n', '2018-02-10 18:33:52,527 - ERROR- An err.\n']

def iterate():
    with open(file_name, "r") as f:
        lines = []
        for line in f:  # read line by line
            lines.append(line)
        print(lines)


# iterate()
# ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n',
#     '2018-02-10 18:33:52,527 - WARNING- An\n', '2018-02-10 18:33:52,527 - ERROR- An err.\n']

with open(file_name, "r") as ins:
    x = [l.strip() for l in ins]
    print(x)
# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log',
#     '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']


