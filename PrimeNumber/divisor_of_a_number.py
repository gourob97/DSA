import math
from logging.config import dictConfig

num = int(input())


# =========== way 1 ========== # 
# checkList = [] 

# for i in range(0,num+1):
#     checkList.append(False)

# checkList[1]=True
# checkList[num] = True

# limit = math.floor(math.sqrt(num))

# for i in range(2,limit):
#     if num%i==0:
#         checkList[i]=True
#         checkList[num//i]=True


# for index,div in enumerate(checkList):
#     if div == True:
#         print(index)




#================
# = way 2 ==================#
limit = math.ceil(math.sqrt(num))
divisors=[]

for i in range(1,limit+1):
    if num%i==0:
        divisors.append(i)
        if num//i not in divisors:
            divisors.append(num//i)

print(len(divisors))



