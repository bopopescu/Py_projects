from __future__ import with_statement
"""
import math
lt = [4, 8 ,9, 11, 15,16,19]
for i in lt:
    sq_n = math.sqrt(i)
    sqrt_floor = math.floor(sq_n)
    sqrt_ceil = math.ceil(sq_n)
    print(i, sq_n, sqrt_floor, sqrt_ceil, sep=", ")
"""


import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

import os
if __name__ == '__main__':
    main()
    print(os.cpu_count())
    print(os.getpid())

# 2.
"""
# concurrent.futures实现进程池和线程池


from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor
import os
import time


def task(n):
    print('{} is running and sleep {} sec'.format(os.getpid(), n))
    time.sleep(n)
    print("wakeup after {} sec".format(n))
    return n ** 2


def solute(res):
    print('solute', res.result(), sep=", ")


if __name__ == '__main__':
    p = ThreadPoolExecutor(max_workers=4)  #
    for i in range(10):
        p.submit(task, i).add_done_callback(solute)  #
    print('*** main test ***')
    for i in range(1,10):
        time.sleep(i)
        print("{} sec later".format(i))

"""

"""
import multiprocessing
import random
import time
def read(q):
    while True:
        try:
            value = q.get()
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        finally:
            q.task_done()

def main():
    q = multiprocessing.JoinableQueue()
    pw1 = multiprocessing.Process(target=read, args=(q,))
    pw2 = multiprocessing.Process(target=read, args=(q,))
    pw1.daemon = True
    pw2.daemon = True
    pw1.start()
    pw2.start()
    for c in [chr(ord('A')+i) for i in range(26)]:
        q.put(c)
    try:
        q.join()
    except KeyboardInterrupt:
        print("stopped by hand")

if __name__ == '__main__':
    main()
"""

"""
from concurrent.futures import ProcessPoolExecutor
#import concurrent


def read(q):
    print('Get %s from queue.' % q)
    time.sleep(random.random())


def main():
    futures1 = set()
    with ProcessPoolExecutor() as executor:
        for q in (chr(ord('A') + i) for i in range(26)):
            future = executor.submit(read, q)
            futures1.add(future)
    try:
        for future in concurrent.futures.as_completed(futures1):
            err = future.exception()
            if err is not None:
                raise err
    except KeyboardInterrupt:
        print("stopped by hand")


if __name__ == '__main__':
    main()
"""
"""

"""
import threading
import time
class Counter():
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000):
        counter.increment()
"""

counter = Counter()
initial_count = counter.get_count()
count_up_100000(counter)
final_count = counter.get_count()
print(final_count)
"""

'''
import threading
counter = Counter()
count_thread = threading.Thread(target=count_up_100000, args=[counter])
#count_thread  = threading.Thread(target=count_up_100000, args=(counter,))
count_thread.start()
mid_join = counter.get_count()
count_thread.join()
after_join = counter.get_count()
print("mid_join _{}".format(mid_join))
print(after_join)
'''
"""
import threading
def conduct_trial(i):
    counter = Counter()
    count_thread = threading.Thread(target=count_up_100000, args=[counter])
    count_thread.start()
    intermediate_value = counter.get_count()
    count_thread.join()
    print("i {} --> inter_value {}".format(i, intermediate_value))
    return intermediate_value

trial1_mid = conduct_trial(1)
print(trial1_mid)
trial2 = conduct_trial(2)
print(trial2)
trial3 = conduct_trial(3)
print(trial3)
"""
'''
i 1 --> inter_value 28077
28077
i 2 --> inter_value 22416
22416
i 3 --> inter_value 37597
37597
'''

##
"""
import threading
def count_up_100000(counter, lock):
    for i in range(10000):
        lock.acquire()
        for i in range(10):
            counter.increment()
        lock.release()

def conduct_trial():
    counter = Counter()
    lock = threading.Lock()
    count_thread = threading.Thread(target=count_up_100000, args=[counter, lock])
    count_thread.start()
    lock.acquire()
    intermediate_value = counter.get_count()
    lock.release()
    count_thread.join()
    print(counter.get_count())
    return intermediate_value

trial1 = conduct_trial()
print(trial1)
trial2 = conduct_trial()
print(trial2)
trial3 = conduct_trial()
print(trial3)
"""
##
""""""
'''
def count_up_100000(counter):
    for i in range(100000):
        counter.increment()

counter = Counter()
count_up_100000(counter)
final_count = counter.get_count()
print(final_count) #100000
count_up_100000(counter)
final_count = counter.get_count()
print(final_count) #200000
'''

"""
"""
"""
def count_up_100000(counter):
    #lock = threading.Lock()
    for i in range(100000):
        lock.acquire()
        counter.increment()
        lock.release()

def conduct_trial():
    counter = Counter()
    count_thread1 = threading.Thread(target=count_up_100000, args=[counter])
    count_thread2 = threading.Thread(target=count_up_100000, args=[counter])

    count_thread1.start()
    count_thread2.start()
    count_thread1.join()
    count_thread2.join()
    final_count = counter.get_count()
    return final_count

for i in range(100):
    lock = threading.Lock()
    trial1 = conduct_trial()
    print(trial1)
    #trial2 = conduct_trial()
    #print(trial2)
    #trial3 = conduct_trial()
    #print(trial3)

"""

"""#####
import threading
class Counter():
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
    def increment(self):
        self.lock.acquire()
        old_count = self.count
        self.count = old_count + 1
        self.lock.release()
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000):
        counter.increment()

def conduct_trial():
    counter = Counter()
    count_thread1 = threading.Thread(target=count_up_100000, args=[counter])
    count_thread2 = threading.Thread(target=count_up_100000, args=[counter])

    count_thread1.start()
    count_thread2.start()

    count_thread1.join()
    count_thread2.join()

    final_count = counter.get_count()
    return final_count

trial1 = conduct_trial()
print(trial1)
trial2 = conduct_trial()
print(trial2)
trial3 = conduct_trial()
print(trial3)
'''
200000
200000
200000
'''
#####
"""
# Example.py
'''
Standard Producer/Consumer Threading Pattern
'''

"""
import time
import threading
from multiprocessing import Queue


class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            # queue.get() blocks the current thread until
            # an item is retrieved.
            msg = self._queue.get()
            # Checks if the current message is
            # the "Poison Pill"
            if isinstance(msg, str) and msg == 'quit':
                # if so, exists the loop
                break
            # "Processes" (or in our case, prints) the queue item
            print("I'm a thread, and I received %s!!" % msg)

        # Always be friendly!
        print('Bye byes!')



def Producer():
    # Queue is used to share items between
    # the threads.
    queue = Queue()

    # Create an instance of the worker
    worker = Consumer(queue)
    # start calls the internal run() method to
    # kick off the thread
    worker.start()

    # variable to keep track of when we started
    start_time = time.time()
    # While under 5 seconds..
    while time.time() - start_time < 5:
        # "Produce" a piece of work and stick it in
        # the queue for the Consumer to process
        queue.put('something at %s' % time.time())
        # Sleep a bit just to avoid an absurd number of messages
        time.sleep(1)

    # This the "poison pill" method of killing a thread.
    queue.put('quit')
    # wait for the thread to close down

    worker.join()
    print("done")


if __name__ == '__main__':
    Producer()
###
"""
"""
### 1
from threading import Thread
import multiprocessing
import time

def countdown(n):
    while n > 0:
        n -= 1

def mult_threads(n):
     t1 = Thread(target= countdown,args=(n//2,))
     t2 = Thread(target= countdown,args=(n//2,))
     t1.start();t2.start()
     print('started')
     t1.join();t2.join()
     print("delay ended")
     #time.sleep(2)

def mult_process(n):
    pn1 = multiprocessing.Process(target=countdown,args=(n//2,))
    pn2 = multiprocessing.Process(target=countdown,args=(n//2,))
    pn1.start();pn2.start()
    pn1.join();pn2.join()


if __name__ == '__main__':
    num = 1000_000_000
    print ('CPU_Cores = :' + str(multiprocessing.cpu_count()))
    #单核串行
    t1_s_time = time.clock()
    countdown(num)
    print ('1 thread 1 Process exec:' + str(time.clock() -t1_s_time))
    #双核2Thread
    t2_s_time = time.clock()
    mult_threads(num)
    print ('2 threads  exec:' + str(time.clock() -t2_s_time))
    #双核2Process
    t3_s_time = time.clock()
    mult_process(num)
    end_time =  time.clock()
    print ('1 Threads 2 Process execTime = ' + str(end_time - t3_s_time) )
"""
"""
## 2.

import multiprocessing
from time import sleep
import time

#work function
def calculate(process_name, tasks, results):
    print("{} evaluation routine starts".format(process_name))
    while True:
        new_value = tasks.get()
        if new_value < 0:
            print("{} evaluation routine quits".format(process_name))
            results.put(-1)
            break
        else:
            compute = new_value * new_value
            sleep(0.02 * new_value)

            print("{} received value: {}".format(process_name, new_value))
            print("{} calculated value: {}".format(process_name, compute))
            results.put(compute)
    return

if __name__ == "__main__":
    manager = multiprocessing.Manager()

    tasks = manager.Queue()
    results = manager.Queue()

    num_processes = 1
    pool = multiprocessing.Pool(processes=num_processes)
    processes = []
    start = time.clock()
    for i in range(num_processes):
        process_name = "P{}".format(i)
        new_process = multiprocessing.Process(target=calculate, args=(process_name, tasks, results))
        processes.append(new_process)
        new_process.start()
    task_list = [43, 1, 780, 256, 142, 68, 183, 334, 325, 3]
    for single_task in task_list:
        tasks.put(single_task)
    sleep(5)
    for i in range(num_processes):
        tasks.put(-1)

    num_finished_processes = 0
    while True:
        new_result = results.get()
        if new_result == -1:
            num_finished_processes += 1
            if num_finished_processes == num_processes:
                print("ALL DONE")
                break
        else:
            print("Result:" + str(new_result))

    print(time.clock() - start)

"""
### 4
"""
import os
import time
import subprocess
start_time = time.clock()
#os.system("TIME OUT /T 15")
subprocess.run(["TIMEOUT", "/T", "4"])
time_lapse = time.clock() - start_time
print("time_lapse is {}".format(time_lapse))
"""
###5
# -*- coding: GBK -*-
"""
#import urlparse
import datetime
import os
from multiprocessing import Process, Queue, Array, RLock


#多进程分块读取文件


WORKERS = 4
BLOCKSIZE = 100000000
FILE_SIZE = 0


def getFilesize(file):
    
###获取要读取文件的大小
    
    global FILE_SIZE
    fstream = open(file, 'r')
    fstream.seek(0, os.SEEK_END)
    FILE_SIZE = fstream.tell()
    fstream.close()

"""
"""
def process_found(pid, array, file, rlock):
    global FILE_SIZE
    global JOB
    global PREFIX
    '''
        进程处理
        Args:
            pid:进程编号
            array:进程间共享队列，用于标记各进程所读的文件块结束位置
            file:所读文件名称
        各个进程先从array中获取当前最大的值为起始位置startpossition
        结束的位置endpossition (startpossition+BLOCKSIZE) 
        if (startpossition+BLOCKSIZE)<FILE_SIZE else FILE_SIZE
        if startpossition==FILE_SIZE则进程结束
        if startpossition==0则从0开始读取
        if startpossition!=0为防止行被block截断的情况，先读一行不处理，从下一行开始正式处理
        if 当前位置 <=endpossition 就readline
        否则越过边界，就从新查找array中的最大值
    '''
    fstream = open(file, 'r')

    while True:
        rlock.acquire()
        print( 'pid%s' % pid, ','.join([str(v) for v in array]))

        startpossition = max(array)
        endpossition = array[pid] = (startpossition + BLOCKSIZE) if (startpossition + BLOCKSIZE) < FILE_SIZE else FILE_SIZE

        rlock.release()
        with open("ax_newtxt.txt", "w") as fw:
            fw.write("WHat happened")
        if startpossition == FILE_SIZE:  # end of the file
            print( 'pid%s end' % (pid))
            break
        elif startpossition != 0:
            fstream.seek(startpossition)
            fstream.readline()
        pos = ss = fstream.tell()
        #ostream = open('ax_test_log_tmp_pid' + str(pid) + '_jobs' + str(endpossition), 'w')
        ostream = open('ax_test_log_tmp_pid.txt' , 'w')
        ostream.write("THis is is")

        while pos < endpossition:
            # 处理line
            line = fstream.readline()
            ostream.write(line)
            pos = fstream.tell()

        print('pid:%s,startposition:%s,endposition:%s,pos:%s' % (pid, ss, pos, pos))

        ostream.flush()
        ostream.close()
        ee = fstream.tell()

    fstream.close()


def main():
    global FILE_SIZE
    print(datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))

    file = "ax_Log_all.txt"
    getFilesize(file)
    print( FILE_SIZE)

    rlock = RLock()
    array = Array('l', WORKERS, lock=rlock)
    threads = []
    for i in range(WORKERS):
        p = Process(target=process_found, args=[i, array, file, rlock])
        threads.append(p)

    for i in range(WORKERS):
        threads[i].start()

    for i in range(WORKERS):
        threads[i].join()

    print(datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))

if __name__ == '__main__':
    main()
"""
###6
"""
import os
import time
from multiprocessing import Pool

def getFile(path) :
  #获取目录下的文件list
  fileList = []
  for root, dirs, files in list(os.walk(path)) :
    for i in files :
      if i.endswith('.txt') or i.endswith('.10w') :
        fileList.append(root + "\\" + i)
  return fileList

def operFile(filePath) :
  #统计每个文件中行数和字符数，并返回
  filePath = filePath
  fp = open(filePath)
  content = fp.readlines()
  fp.close()
  lines = len(content)
  alphaNum = 0
  for i in content :
    alphaNum += len(i.strip('\n'))
  return lines,alphaNum,filePath

def out(list1, writeFilePath) :
  #将统计结果写入结果文件中
  fileLines = 0
  charNum = 0
  fp = open(writeFilePath,'a')
  for i in list1 :
    fp.write(i[2] + " #line："+ str(i[0]) + " #chars："+str(i[1]) + "\n")
    fileLines += i[0]
    charNum += i[1]
  fp.close()
  print(fileLines, charNum)

if __name__ == "__main__":
  #创建多个进程去统计目录中所有文件的行数和字符数
  startTime = time.time()
  filePath = os.getcwd()
  fileList = getFile(filePath)
  pool = Pool(5)
  resultList =pool.map(operFile, fileList)
  pool.close()
  pool.join()

  writeFilePath = "new_res.txt"
  print(resultList)
  out(resultList, writeFilePath)
  endTime = time.time()
  print ("used time is ", endTime - startTime)

"""
###7
"""
import multiprocessing as mp
def job(q):
    res = 0
    for i in range(1000):
        res += i + i**i + i**3
    q.put(res)

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args = (q,))
    p2 = mp.Process(target=job, args = (q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print("res1 is {},\n res2 is {}".format(res1,res2))
"""

###9
"""
import multiprocessing as mp
def job(x):
    return x*x
def multicore():
    pool = mp.Pool(processes=4)
    res = pool.map(job, range(10))# map returns results
    print("res is {}".format(res))
def multicore_2():
    pool = mp.Pool(processes = 4)
    res = pool.apply_async(job,(2,))
    print(res.get())

    mul_res = [pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in mul_res])

if __name__ == '__main__':
    multicore()
    multicore_2()
"""
###10
"""
import threading
from time import sleep, ctime
import datetime

loops = [4,2]


def loop(nloop, nsec):
    print("start loop" + str(nloop) + "at: " + str(ctime()))
    sleep(nsec)
    print("loop {} is done at {}".format(nloop, ctime()))
#
def main():
    print("starting at: {}".format(ctime()))
    threads =[]
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print("all Set {}".format(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")))

if __name__ == '__main__':
    main()
"""
###10
"""
#from __future__ import with_statement
import threading
from time import sleep,ctime

lock = threading.Lock()
loops = [4,2]

def loop(nloop,nsec):
    with(lock):
        #lock.acquire()
        print('start loop '+str(nloop)+' at : '+str(ctime()))
        #lock.release()
    sleep(nsec)
    print('loop ',nloop,' done at : ',ctime())

def main():
    print('starting at : ',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at : ',ctime())

if __name__ == '__main__':
    main()
"""
###10
"""
from time import ctime
import threading

def coding(language):
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(5):
        print('I\'m coding ',language, ' program at ', ctime() )

def music():
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(5):
        print('I\'m listening music at ', ctime())

if __name__ == '__main__':

    print('thread %s is running...' % threading.current_thread().name)

    thread_list = []
    t1 = threading.Thread(target=coding, args=('Python',))
    t2 = threading.Thread(target=music)
    thread_list.append(t1)
    thread_list.append(t2)

    for t in thread_list:
        t.setDaemon(True)  # 设置为守护线程
        t.start()
        #print('thread %s is running...' % threading.current_thread().name)
        t.join()  # 在这个子线程完成运行之前，主线程将一直被阻塞

    print('thread %s ended.' % threading.current_thread().name)
"""
###11
"""
import threading

money = 0 # 变量 money 被 t1和 t2 两个线程共享

# 存钱
def put_money(sum):
    global money
    money += sum

# 取钱
def get_money(sum):
    global money
    money -= sum

def run_thread(sum):
    for i in range(1000000): #执行的次数要足够多
        # 先存sum，后取sum，钱数应当为0
        put_money(sum)
        get_money(sum)

t1 = threading.Thread(target=run_thread, args=(100,))
t2 = threading.Thread(target=run_thread, args=(1000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(money)
"""
#12
"""
from multiprocessing import Process, Queue
import os

# 一个进程写数据
def write(q):
    for i in range(100):
        print('Write', i)
        q.put(i)

# 另一个进程读数据:
def read(q):
    while True:
        value = q.get(True)
        print('Read', value)

if __name__ == '__main__':

    print('parent process %s is running...' % os.getpid())

    # 在父进程中创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate() # 强行终止pr进程

    print('child process stop')
"""
###13
