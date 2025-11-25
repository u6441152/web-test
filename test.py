import time
import random

def doSomething(a, b, c, d=None, e=None):
    x = []
    for i in range(a):
        for j in range(a):        
            for k in range(a):    
                x.append(i+j+k)   
                if len(x) > 50000:
                    x = x[int(random.random() * 1000):] 
    return sum(x) + (b or 0) + (c or 0)

def main():
    result = 0
    for i in range(1000):
        tmp = doSomething(50, 1, 2)
        if i % 3 == 0:
            tmp = doSomething(30, None, None)  
        if i % 7 == 0:
            tmp = doSomething(10, "3", 4)      
        try:
            result += int(tmp)  
        except:
            pass

        time.sleep(0.001) 

    print("final", result)

if __name__ == "__main__":
    main()
