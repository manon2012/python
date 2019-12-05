
import threading
import time

def fun(n):
    time.sleep(2)
    print(n)



if __name__ == '__main__':

    t1=threading.Thread(target=fun,args=(123,))
    t2=threading.Thread(target=fun,args=(345,))

    t1.start()
    t2.start()
    print(t1.name,t1.is_alive(),t1.ident)



    print ('main func')
