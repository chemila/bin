import threading

class mythread(threading.Thread):

    def __init__(self, name):
        self.sname = name
        threading.Thread.__init__(self)

    def run(self):
        print self.sname
        for i in range(5): print i

stdoutmutex = threading.Lock()
threads = []

for i in range(10):
    thread = mythread('thread %d' % i)
    threads.append(thread)
    thread.start()

for thread in threads: thread.join()
print 'end main'
