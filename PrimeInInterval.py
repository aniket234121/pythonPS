print("enter the interval to find prime no.")
start=int(input("enter the starting no."))
end=int(input("enter the ending no."))
print("prime no from ",start," to ",end," are: ")
if(start<end):
    for i in range(start,end,1):
        num=i
        count=0
        while(num!=0):
            if(i%num==0):
                count=count+1
            num=num-1
        if(count<=2):
            print(i)
else:
    print("starting no is bigger than end")
