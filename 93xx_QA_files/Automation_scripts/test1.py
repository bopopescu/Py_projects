##import time, os
##def jobx():
##    print "this is it";
##    time.sleep(5);
##    jobx();
##
##print "ready"
##jobx();


##import time
##from threading import Timer
##
##def print_time():
##    print "From print_time", time.time()
##def print_some_time():
##    print time.time()
##    Timer(5, print_time, ()).start()

#1. scheduler

##import sched, time;
##time.sleep(10);
##print "first time is ", time.time()
###s = sched.scheduler(time.time, time.sleep)
##time.sleep(10);
##print "2nd time is ", time.time();
##
##counter = 0;
##run = False;
##
##def print_time():
##    print "Enter print_time: ", time.time()
##    global run;
##    if run:
##        return
##    
##    time.sleep(10);
##    global counter
##    counter = counter + 1
##    print "counter is ", counter
##    print "From print_time", time.time();
##
##def print_some_times():
##    print time.time();
##    s = sched.scheduler(time.time, time.sleep)
##    s.enter(2, 1, print_time, ());
##    s.enter(40, 1, print_time, ());
##    s.run();
##    print time.time();
##
##print_some_times();


import os;

print \
      "*****************************\
        TEST is DONE \
       *****************************"
     
        

    
      

