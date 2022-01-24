import math
from cgitb import reset

num = int(input())


checklist =[]
prime=[]
for i in range(0,num+1):
    checklist.append(True)
checklist[0] = False 
checklist[1] = False

limit = math.floor(math.sqrt(num))+1

for i in range(2,limit):
    if checklist[i]==False:
        continue
    j=i+i 
    while j<num+1:
        checklist[j]= False
        j=j+i

for index, bool in enumerate(checklist):
    if bool == True:
        prime.append(index)

prime_divisors = []
for div in prime:
    while num%div==0 and num!=1:
        prime_divisors.append(div)
        num/=div

print(prime_divisors)
