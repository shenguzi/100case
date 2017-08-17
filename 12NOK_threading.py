import threading
import time

exitFlag = 0

class myThread (threading.Thread):
#继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self): #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
     print( "Starting " + self.name)
     print_time(self.name, self.counter, 5)
     print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
# 开启线程
thread1.start()
thread2.start()
print( "Exiting Main Thread")


def worker():
    print “worker”

    time.sleep(1)

    return


for i in xrange(5):
    t = threading.Thread(target=worker)

    t.start()

这段代码就使用了多线程，但是没法传递参数，而实际使用多线程，往往是需要传递参数的，于是问了一位群里的网友后，知道可以这么写实现传递参数的多线程：

import threading

import time


def worker(number):
    print “worker”

    time.sleep(number)

    return


for i in xrange(5):
    t = threading.Thread(target=worker, args=(i,))

    t.start()

第一个参数是线程函数变量，第二个参数args是一个数组变量参数，如果只传递一个值，就只需要i, 如果需要传递多个参数，那么还可以继续传递下去其他的参数，其中的逗号不能少，少了就不是数组了，就会出错。




