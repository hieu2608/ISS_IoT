from threading import Thread
import sys, time

class thread2(object):
    def __call__(self, left, right, duration):
        for i in range(12):
            time.sleep(duration)
            print "%s%d%s " % (left,i,right),
            sys.stdout.flush()

t2 = Thread(target=thread2(), args=('[',']', 1))
t2.start()
t = thread2()
t('<','>', 1.5)