N=int(input("enter the nth term to find fibonacci no."))
num1=0
num2=1
for i in range(3,N+1,1):
    f=num1+num2
    num1=num2
    num2=f
print(f," is nth fibonacci term")