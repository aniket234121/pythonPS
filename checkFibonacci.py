import math
num=int(input("enter a no. to check the number is fibonacci number:"))
x=(num*num*5)+4
y=(num*num*5)-4
x1=int(math.sqrt(x))
y2=int(math.sqrt(y))
if(x1*x1==x):
    print(num," is fibonacci no.")
elif(y2*y2==y):
    print(num," is fibonacci no.")
else:
    print(num," is not fibonacci no.")
