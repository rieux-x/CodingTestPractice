import math 

def solution(n):
    answer = 0
    
    for i in range(2,n+1):
        
        isPrime = True
        
        for j in range(2, int(math.sqrt(i)) + 1 ):
            if i%j==0:
                isPrime = False
                break
                
        if isPrime == True:
            answer = answer + 1
            
    return answer