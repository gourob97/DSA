# import math
# num = int(input())

# numlist =[]
# checklist =[]
# for i in range(0,num+1):
#     numlist.append(i)
#     checklist.append(True)
# checklist[0] = False 
# checklist[1] = False

# limit = math.floor(math.sqrt(num))+1

# for i in range(2,limit):
#     j=i+i 
#     while j<num+1:
#         checklist[j]= False
#         j=j+i
    
# for index,n in enumerate(numlist):
#     ans = "not prime" if checklist[index]==False else "prime"
#     if ans == "prime":
#         print(str(n)+'--> '+ans)
    
    
    
import math
num = int(input())


checklist =[]
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
    
for index,n in enumerate(checklist):
    ans = "not prime" if checklist[index]==False else "prime"
    if ans == "prime":
        print(str(index)+'--> '+ans)
    
    
    
    
    

    
#O(nloglogn)