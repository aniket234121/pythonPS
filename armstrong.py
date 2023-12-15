print("program to check for armstrong no.")
num=int(input("enter the no. "))
# digit=0,sum=0,t=num,count=0
t=num
count=0
while(t!=0):
    digit=t%10
    t=t//10
    count=count+1;
t=num
sum=0
while(t!=0):
    digit=t%10
    t=t//10
    sum=sum+digit*digit*digit;
if(sum==num):
    print(num," is armstrong no.")
else:
    print(num,"is not armstrong no.")