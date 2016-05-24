from threading import Thread
import time, sys

def thread1(left, right, duration):
    for i in range(12):
        time.sleep(duration)
        print "%s%d%s " % (left,i,right),
        sys.stdout.flush()

t1 = Thread(target=thread1, args=('[',']', 1))
t1.start()
thread1('<','>', 1.5)