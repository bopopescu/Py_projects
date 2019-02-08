from pprint import pprint
def combinations(*list):
    """ Returns a list of all combination of input list """
    r = [[]]
    for x in list:
        r = [ i + [y] for y in x for i in r ]
        #print ">>>> r = ",r
    return r
def getParamCombinations(rawParamList):
    ''' Returns a list of lists, in which each item in the list is a unique
        combination of parameter values.  The list represents all possible
        combinations of the parameter values.  A sub-item in a list may be
        a list itself, representing a "section" which is iterated over within
        that test.
        rawParamList : a list of lists, in which each primary item in the
                       list represents the values for one parameter that
                       will be iterated.
        Example: rawParamList = [[2412, 2417, 2422], ['OFDM_6', 'OFDM_12'],
            ['TX_VERIFY_EVM', 'TX_VERIFY_MASK', 'RX_VERIFY_PER' ], ['15.2', '14.7'],
            ['(0,1,0,0)', '(1,0,0,0)']]
        Output:  [2412, 'OFDM_6', 'TX_VERIFY_EVM', '15.2', '(0,1,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_EVM', '15.2', '(1,0,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_EVM', '14.7', '(0,1,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_EVM', '14.7', '(1,0,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_MASK', '15.2', '(0,1,0,0)']
                 ....
    '''
    plist = rawParamList
    # We reverse the list, because combinations() will iterate starting
    # from the last item, and we want to preserve the user's intended
    # iteration order as specified from left to right (first to last).
    # However this reverses the order of the parameters, so after running
    # combinations() we reverse each item in the combos list to get the
    # original parameter order back.
    # I wonder if combinations() could be changed so that this reversing
    # is not necessary.  I have not spent time looking into that.
    plist.reverse()
    # call the raw combination generator
    combos = combinations(*plist)
    # we don't sort anymore because reversing works better
    #combos.sort()
    for tlist in combos:
        tlist.reverse()
    return combos

def check_log_error(log_file):
    err_occur = []
    substr = "Fail"
    try:
        with open (log_file, 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if line.lower().find(substr) != -1:
                    err_occur.append((linenum, line.rstrip('\n')))
            for linenum, line in err_occur:
                print("Line ", linenum, ": ", line)
    except FileNotFoundError:
        print("Log file not found.")
def check_error_re(log_file):
    import re
    err_occur = []
    pattern = re.compile('error', re.IGNORECASE)
    try:
        with open('logfile.txt', 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if pattern.search(line) != None:
                    err_occur.append( (linenum, line.rstrip('\n')))
            for linenum, line in err_occur:
                 print("Line ", linenum, ": ", line)
    except FileNotFoundError:
        print("Log file not found.")
def test_log():
    import re
    pattern = re.compile(r"(\+\d{1,2})?[\s.-]?\d{3}[\s.-]?\d{4}")
    try:
        with open ('info.txt', 'rt') as in_file:
            for linenum, line in enumerate(in_file):
                if pattern.search(line) != None:
                    err_occur.append((linenum, line.rstrip('\n')))
            for linenum, line in err_occur:
                print("Line ", linenum, ": ", line)
    except FileNotFoundError:
        print("Input file not found.")
def check_matrix(m):
    import pprint
    print("rows is {}".format(len(m)))
    print("col is {}".format(len(m[0])))
    pprint.pprint(m)
if __name__ == "__main__":
    rawParamList = [[2412, 2417, 2422],
                    ['OFDM_6', 'OFDM_12'],
                    ['TX_VERIFY_EVM', 'TX_VERIFY_MASK', 'RX_VERIFY_PER'],
                    ['15.2', '14.7'],
                    ['(0,1,0,0)', '(1,0,0,0)']]
    combo = getParamCombinations(rawParamList)
    for i in combo:
        #print (i)
        pass
    import pprint
    m = [[x+y for x in range(3)] for y in range(10)]
    #
    #pprint.pprint(m)
    #m = [0 for x in range(3)]
   # print (m)
   # print(type(m))
    import re
    str = 'flog resulTwtd'
    pat = re.compile(r"\bl\w*t", re.IGNORECASE)
    if pat.search(str) != None:
        print("found")
   #for i in len(m[0]):
    #    pass
        #print(m[i])
    #print(m[0])
    #print(len(m[0]))
    #print(len(m))
    check_matrix(m)
