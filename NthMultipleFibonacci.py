num=int(input("enter the number :"))
multiple=int(input("enter the Nth multiple to find :"))
count=2
a=0
b=1
sum=0
pos=2
while(multiple!=0):
    
    sum=a+b
    a=b
    b=sum
    pos=pos+1
    print(sum,pos)
    if(sum%num==0):
        multiple=multiple-1
print("position in fibonacci no. :",pos," and value is : ",sum)