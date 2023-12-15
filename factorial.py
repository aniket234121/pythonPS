print("to print the factorial of given no.")
num=int(input("enter the no to find factorial"))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
print(fact)