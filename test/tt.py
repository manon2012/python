
import threading
from threading import Thread
from time import ctime,sleep

def music(f):
    for i in range(2):
        print( "muisc !!!%s time %s"%(f,ctime()))
        sleep(1)

def movie(f):
    for j in range(2):
        print("movie  %s time%s"%(f,ctime()))
        sleep(2)

class tt(Thread):
    def __init__(self,name="python"):
        super(tt, self).__init__()
        self.name= name
    def run(self):
        print ("hello",self.name)




threads =[]
t1= threading.Thread(target=music,args=('1997',))
threads.append(t1)
t2= threading.Thread(target= movie,args=('2012',))
threads.append(t2)
print(threads)
if __name__ == '__main__':
    # music("1997")
    # movie("2012")
    # print ("all %s"%ctime())
    for i in threads:
        i.setDaemon(True)
        i.start()
        print("it's a thread%s" % threading.current_thread())

    print(threading.active_count())
    i.join()
    print("all %s" % ctime())

    tt1=tt()
    tt2=tt("tt2")
    tt1.start()
    tt2.start()

