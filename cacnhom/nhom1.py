def ham(n):
    gt=1
    for i in range(1,n+1):
        gt=gt*i
    return gt
n=int(input())
print(ham(n))