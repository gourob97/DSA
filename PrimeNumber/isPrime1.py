def isPrime(num):
    if num<2:
        return "not prime"

    for i in range(2,num-1):
        if num%i==0:
            return "not prime"

    return "Prime"

while True:
    num = int(input())
    print(isPrime(num))

