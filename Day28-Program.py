#Day28
# 1 Define a subclass using threading.Thread class.
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class MyThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None): 
        super(MyThread,self).__init__(group=group, target=target, 
			              name=name, verbose=verbose)
	self.args = args
	self.kwargs = kwargs
	return

    def run(self):
	    logging.debug('running with %s and %s', self.args, self.kwargs)
	    return

if __name__ == '__main__':
    for i in range(3):
	    t = MyThread(args=(i,), kwargs={'a':1, 'b':2})
	    t.start()

#2 Instantiate the subclass and trigger the thread.

from _thread import start_new_thread
from time import sleep

threadId = 1 # thread counter
waiting = 2 # 2 sec. waiting time

def factorial(n):
    global threadId
    rc = 0
    
    if n < 1:   # base case
        print("{}: {}".format('\nThread', threadId ))
        threadId += 1
        rc = 1
    else:
        returnNumber = n * factorial( n - 1 )  # recursive call
        print("{} != {}".format(str(n), str(returnNumber)))
        rc = returnNumber
    
    return rc

start_new_thread(factorial, (5, ))
start_new_thread(factorial, (4, ))

print("Waiting for threads to return...")
sleep(waiting)