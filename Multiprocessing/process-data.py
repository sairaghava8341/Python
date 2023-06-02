import multiprocessing as mp

result=[]

def calculate_square(arr):
    global result
    for i in arr:
        result.append(i*i)
    print("Inside",str(result))
  
if __name__=="__main__":
    arr=[i for i in range(50)]
    p1=mp.Process(target=calculate_square,args=(arr,))
    p1.start()
    p1.join()
    print("main",str(result))

    