temp= 0 
def number(num1,num2,num3):
    if num1<=num2 and num1<=num3:
        if num2<=num3:
            return num1,num2,num3
        else:
            return num1,num3,num2
    elif num2<=num1 and num2 <=num3:
        if num1<=num3:
            return num2,num1,num3
        else:
            return num2,num3,num1
    else:
        if num1<=num2:
            return num3,num1,num2
        else:
            return num3,num2,num1        


x=int(input("x= "))
y=int(input("y= "))
z=int(input("z= "))
print ("số gốc:",x, y, z)
print ("số đã sắp xếp:",number(x,y,z))

