from threading import Thread
import sys, time
from thread1 import thread1

class thread3(Thread):
  def run(self):
    duration = int(self._Thread__args[2])
    for i in range(12):
      time.sleep(duration)
      print "%s%d%s "%(self._Thread__args[0],i,self._Thread__args[1]),
      sys.stdout.flush()

t3 = thread3(args=('{','}', 1))
t3.start()
thread1('<','>', 1.5)