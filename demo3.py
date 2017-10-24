# Python多线程

import threading
from time import ctime, sleep


def music(name):
    for i in range(2):
        print("I was listening to %s.  %s" % (name, ctime()))
        sleep(1)


def movie(name):
    for i in range(2):
        print("I was watching the %s.  %s" % (name, ctime()))
        sleep(5)


threads=[]
#args是一个元组
t1=threading.Thread(target=music,args=("第三人称",))
threads.append(t1)
t2=threading.Thread(target=movie,args=("心理罪",))
threads.append(t2)

if __name__=='__main__':
    for t in threads:
        t.start()

    #主线程和子线程同时开始，join()表示等子线程执行完后才执行主线程，如果去掉后则主线程执行完后，子线程也必须停止
    t.join()
    print("over.... %s" % ctime())