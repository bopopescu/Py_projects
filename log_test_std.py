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
#299
# aa = "abcd"
# print(set(aa))

def getHint(secret, guess):
    dic_s, dic_g = {}, {}
    cnt_c, cnt_b = 0, 0
    for i, val in enumerate(secret):
        #val = int(val)
        if val == guess[i]:
            cnt_b +=1
        else:
            dic_s[val] = dic_s[val] + 1 if val in dic_s else 1
            dic_g[guess[i]] = dic_g[guess[i]] + 1 if guess[i] in dic_g else 1
    for key, val in dic_s.items():
        #key, val = int(key), int(val)
        if key in dic_g:
            cnt_c += val if val <= dic_g[key] else dic_g[key]
    return str(cnt_b) + "A" + str(cnt_c) + "B"


print(getHint("1123",'0111'))

def run_flow1(run_dir, flow_to_test, result_dir):
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


st = "qa test on package 4.40.0.23"


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

#1025
import copy
lst = ['wifi','Bt','ax', 'Ac', 'bde']
# add, remove, search, sort,
s = "WifiBT11AC11AXrsdbz"
print(lst)


#+
lst.append("ax_5G")
# print(lst)
lst.insert(1, "ax_7G")
print(lst)
#rst = copy.deepcopy(lst)
rst = lst.index("Bt")
print(rst)

print(lst.pop(), lst, sep="::" )
#859
def buddyStrings(A,B):
    cnt = -1
    if len(A) != len(B):
        return False
    if A == B:
        if len(A) == len(set(A)):
            return False
        return True
    for i in range(len(A)):
        if A[i] != B[i]:
            if cnt == -1:
                rst = i
                cnt = 1
            elif cnt == 1:
                if A[i] == B[rst] and A[rst] == B[i]:
                    cnt = 0
                else:
                    return False
            else:
                return False
    return cnt == 0


















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


