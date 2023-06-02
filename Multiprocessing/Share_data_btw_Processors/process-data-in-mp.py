import multiprocessing as mp



def calculate_square(arr,result):
    
    for i,num in enumerate(arr):
        result[i]=num*num
        
  
if __name__=="__main__":
    arr=[i for i in range(50)]
    result=mp.Array("i",50)
    p1=mp.Process(target=calculate_square,args=(arr,result))
    p1.start()
    p1.join()
    print(result[:])

    