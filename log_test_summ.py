from pprint import pprint
from collections import Counter
import time
import time
s="cbaebabacd"
p = "abc"
def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line
def run_flow(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode
from collections import deque, Counter
from pprint import pprint
#########list
arr = ['Wifi','bt','ax','Rsdb']
add_v = "uwb"
# arr.append(add_v)
# arr += add_v
# arr.insert(1, add_v)
##
# arr.pop()
# arr.remove("wifi")
##
# print(arr.index('bt'))
##
# arr_sorted = sorted(arr, key=len)
#arr_sorted = sorted(arr, key=str.lower)
# arr_sorted = sorted(arr, reverse=True)
##
# print(arr[:],arr[:2], arr[:-1],arr[::-1],arr[3:0:-1], arr[:0:-1], sep="\n")
#######dic
dct = {1:"wifi", 2:"bt", 3:"ax", 4:"rsdb"}
dct[5] = "ac"
dct_tuple = [(6, 'bgn'), (7, 'uwb'), (8, 'n')]
dct.update(dct_tuple )
dct_1 = dict(dct_tuple)

# dct.pop(3)
# dct.popitem()
for k, v in dct.items():
    print(k, v)

###set
st = ['wifi','bt','ac','ax']
st = set(st)

st.add("uwb")
st.update(["b",'g','n'])

st.remove('n')
st.discard('ax')
st.pop()
print(st)

###
def minim(*n):
    print(type(n))
    if n:
        mn = n[0]
        # print(mn)
        for v in n[1:]:
            # print(v)
            mn = v if mn > v else mn
    print("mn is {}".format(mn))
# minim(*(1,3,0,-1))
#minim(1,3,0,-1)
# minim((1,3,0,-1))

####
def func_vKwargs(**kwargs):
    print(kwargs)

func_vKwargs(a=1, b=2)
func_vKwargs(**{'wifi':1, "bt":2})
func_vKwargs(**dict([("wifi",1),("bt", 2)]))
###

def divide_tup(a,b):
    return a//b, a/b

rst = divide_tup(10,5)
print("type is {0} and rst is {1}".format(type(rst), rst))
print(dir(list(divide_tup)))
###
def get_squares(n): # classic function approach
    return [x ** 2 for x in range(n)]
print(get_squares(10))

def get_squares_gen(n):  # generator approach
    for x in range(n):
        yield x ** 2  # we yield, we don't return
print(list(get_squares_gen(10)))

###
def get_square(n):
    for i in range(n):
        yield i**2
sq = get_square(5)
# for i in sq:
#     print(i, end=", ")
sq = list(sq)
print(sq)
###
def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k += 1

for n in geometric_progression(2, 5):
    if n < 100:
        print(n)
print("*"*10)
for n in geometric_progression(2,5):
    if n > 100:
        print(n)
###

###
def run_flow(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1) #TreeNode

def copy_setup_file(run_dir, setupfile_loc):
    for setup_file in os.listdir(setupfile_loc):
        src = os.path.join(setupfile_loc, setup_file)
        shutil.copy2(src, run_dir)


def copy_flows(run_dir, flow_to_test, flowfile_loc ):
    for flow_name in os.listdir(flowfile_loc):
        #flow_name = os.path.split(flow_name)[-1]
        flow_name  = flow_name.split("\\")[-1]
        src = os.path.join(flowfile_loc, flow_name)
        shutil.copy2(src, run_dir)
        flow_to_test.append(flow_name)


