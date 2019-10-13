
file_name = "logging_test.txt"
with open(file_name, 'r') as infile:
    text_str = infile.read() # read in as a single string
    text = text_str.splitlines()# a list of strings stripped of "\n"
    # print(text_str)

# 2018-02-10 18: 33: 52, 527 - DEBUG - End
# 2018-02-10 18: 33: 52, 527 - INFO - The log
# 2018-02-10 18: 33: 52, 527 - WARNING - An
# 2018-02-10 18: 33: 52, 527 - ERROR - An err

    print("\n\n\n")
    # print(text)
print("#________________________________________")
print("#________________________________________")

# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log',
#     '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']
def iterate():
    with open(file_name, "r") as f:
        lines = []
        for line in f: # read line by line
            lines.append(line)
        print(lines)
        # ['2018-02-10 18:33:52,527 - DEBUG- End\n', '2018-02-10 18:33:52,527 - INFO- The log\n',
        #  '2018-02-10 18:33:52,527 - WARNING- An\n', '2018-02-10 18:33:52,527 - ERROR- An err.\n']
# iterate()
print("#________________________________________")
print("#________________________________________")
def iterate1():
    with open(file_name, 'r') as infile:
        lines = [ line.strip() for line in infile]
        print(lines)
# iterate1()
# ['2018-02-10 18:33:52,527 - DEBUG- End', '2018-02-10 18:33:52,527 - INFO- The log',
#  '2018-02-10 18:33:52,527 - WARNING- An', '2018-02-10 18:33:52,527 - ERROR- An err.']
print("#________________________________________")
print("#________________________________________")
