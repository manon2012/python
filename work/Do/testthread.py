import threading
import time
def movie():
    time.sleep(2)
    print ('movie show')
def music():
    time.sleep(1)
    print ('music show')

if __name__ == '__main__':
    t1=threading.Thread(target=movie,args=())
    t2=threading.Thread(target=music,args=())
    # t1.daemon=True
    # t2.daemon=True
    alist=[]
    alist.append(t1)
    alist.append(t2)
    for i in alist:
        i.start()
        i.join()

    print("in main")

