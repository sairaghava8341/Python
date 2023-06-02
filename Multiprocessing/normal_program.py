import time

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
        res_cube.append(i*i)
    print(res_cube)

if __name__=="__main__":
    arr=[i for i in range(50)]
    start=time.time()
    calculate_square(arr)
    calculate_cube(arr)
    end=time.time()
    print(f"Time Taken:{round(end-start,2)}")