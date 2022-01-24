import math

def isPrime(num):
    if num<2:
        return "not prime"
    if num==2:
        return "Prime"
    
    if num%2==0:
        return "not prime"
    
    limit = math.ceil( math.sqrt(num+1) )  #for precision

    for i in range(3,limit,2):
        if num%i==0:
            return "not prime"

    return "Prime"

while True:
    num = int(input())
    print(isPrime(num))

#time complexity O(n/2) = O(n)