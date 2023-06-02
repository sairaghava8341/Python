import multiprocessing as mp
import time 


def deposit(balance,l):
    for i in range(1000):
        time.sleep(0.01)
        l.acquire()
        balance.value=balance.value+1
        l.release()


def withdraw(balance,l):
    for i in range(1000):
        time.sleep(0.01)
        l.acquire()
        balance.value=balance.value-1
        l.release()

        
  
if __name__=="__main__":
    balance=mp.Value("i",200)
    l=mp.Lock()
    p1=mp.Process(target=deposit,args=(balance,l))
    p2=mp.Process(target=withdraw,args=(balance,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(balance.value)

    