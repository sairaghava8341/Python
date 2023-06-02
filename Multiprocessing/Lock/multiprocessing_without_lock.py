import multiprocessing as mp
import time 


def deposit(balance):
    for i in range(1000):
        time.sleep(0.01)
        balance.value=balance.value+1


def withdraw(balance):
    for i in range(1000):
        time.sleep(0.01)
        balance.value=balance.value-1

        
  
if __name__=="__main__":
    balance=mp.Value("i",200)
    p1=mp.Process(target=deposit,args=(balance,))
    p2=mp.Process(target=withdraw,args=(balance,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(balance.value)

    