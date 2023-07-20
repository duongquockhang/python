# import math
# def snt(a):
#     for i in range(2,round(math.sqr(a))+1):
#         if a % i == 0:
#             return False
#         return True
# n=int(input('n='))
# if snt(n):
#     print('la so nguyen to')
# else:
#     print('khong la so nguyen to')
 
def snt(a):
    dem=0
    for i in range(1,a+1):
        if a % i == 0:
            dem+=1
    if dem == 2:
        print('so nguyen to')
    else:
        print('ko la so nguyen to') 
n=int(input('n='))
snt(n)
