from multiprocessing import Pool
import time

def func(n):
    sum=0
    for i in range(10000):
        sum+=i*i

if __name__=="__main__":

    t1=time.time()
    p=Pool()
    result=p.map(func,range(10000))
    p.close()
    p.join()

    print("pool took:",time.time()-t1)

    t2=time.time()
    result=[]
    for i in range(10000):
        result.append(func(i))

    print("Serial Processing took:",time.time()-t2)
