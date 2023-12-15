num=int(input("enter a  no. to check prime no."))
t=num
count=0
while(t!=0):
    if(num%t==0):
        count=count+1
    t=t-1
if(count<=2):
    print(num," is prime no.")
else:
    print(num," is not prime no.")