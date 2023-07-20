a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if (a> b):
    if(a>c):
        print ('a max')
    else:
        if c>b:
            print('c max')
        else:
            print('b max')       
else:
    if b>c:
        print('b max')
    else:
        print('c max')
