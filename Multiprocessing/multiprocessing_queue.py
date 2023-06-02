import multiprocessing as mp



def calculate_square(arr,q):
    for i in arr:
        q.put(i*i)
        
  
if __name__=="__main__":
    arr=[i for i in range(50)]
    q=mp.Queue()
    p1=mp.Process(target=calculate_square,args=(arr,q))
    p1.start()
    p1.join()
    
    while q.empty() is False:
        print(q.get())

    