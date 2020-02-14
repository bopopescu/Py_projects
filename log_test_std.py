from pprint import pprint
from collections import Counter
import time
import time

# 1/30, 2/3,2/10
#_____________________________________________

#_____________________________________________

# 611
def triangleNumber(self, nums: List[int]) -> int:
    # 2/11 9:22 --> 9:43
    cnt = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            sum_two = nums[i] + nums[j]
            lt, rt = j + 1, n - 1
            while lt < rt:
                mid = lt + (rt - lt) // 2
                if nums[mid] > sum_two:
                    rt = mid
                else:
                    lt = mid + 1
            if lt == rt:
                if j == n - 2 and sum_two > nums[n - 1]:
                    cnt += 1
                elif j != n - 2:
                    cnt += n - 1 - rt + 1

    return cnt

#_____________________________________________
    def triangleNumber(self, nums: List[int]) -> int:
        # 2/11 9:22 --> 9:43
        cnt = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                sum_two = nums[i] + nums[j]
                lt, rt = j + 1, n
                mid = 0
                while lt < rt:
                    mid = lt + (rt - lt) // 2
                    if nums[mid] < sum_two:
                        lt = mid + 1
                    else:
                        rt = mid
                cnt += rt - j - 1

                # if lt == rt:
                #     cnt += lt - j +1

                # if j == n-2 and sum_two > nums[n-1]:
                #     cnt += 1
                # elif j != n-2 and sum_two > nums[mid]:
                #     cnt += n-1-rt + 1

        return cnt
#_____________________________________________
n = len(nums)
        nums.sort()
        cnt = 0
        # for i in range(n-1,3,-1): bug
        for i in range(n-1,1,-1):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    cnt += right - left
                    right -= 1
                else:
                    left += 1
        return cnt
#_____________________________________________

#_____________________________________________

#_____________________________________________

#_____________________________________________

#_____________________________________________


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

def run_flow2(run_dir, flow_to_test, result_dir):
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

