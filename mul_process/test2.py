import threading
from time import sleep, ctime
lock = threading.Lock()
test_list = [4,2]

def loop(run, nsec):
    lock.acquire()
    print('start run '+ str(run)+' at : '+ str(ctime()))
    sleep(nsec)
    lock.release()
    sleep(1)
    print('run ',run ,' done at : ', ctime())

def main():
    print('starting at : ',ctime())
    threads = []
    runs = range(len(test_list))

    for run in runs:
        t = threading.Thread(target=loop, args=(run,test_list[run]))
        threads.append(t)

    for i in runs:
        threads[i].start()

    for i in runs:
        threads[i].join()

    print('all DONE at : ',ctime())

if __name__ == '__main__':
    main()