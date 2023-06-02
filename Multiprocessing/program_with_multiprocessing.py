import time
import multiprocessing as mp

def calculate_square(arr):
    res_sq=[]
    for i in arr:
        #print(f"Square:{i*i}")
        time.sleep(0.2)
        res_sq.append(i*i)
    print(res_sq)

def calculate_cube(arr):
    res_cube=[]
    for i in arr:
        #print(f"Cube:{i*i*i}")
        time.sleep(0.2)
        res_cube.append(i*i*i)
    print(res_cube)

if __name__=="__main__":
    arr=[i for i in range(50)]
    #start=time.time()
    p1=mp.Process(target=calculate_square,args=(arr,))
    p2=mp.Process(target=calculate_cube,args=(arr,))
    start=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.time()
    print(f"Time Taken:{round(end-start,2)}")