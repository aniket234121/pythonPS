str1 =input("enter the list 1 seprated by spaces");
mylist=str1.split()
count=0
flag=0
def checkPrime(list):
    for i in list:
        n=i
        
        while(i!=0):
            if(n%i==0):
            count=count+1
        
        if(count<=2):
            flag=1
        else:
            flag=0
if(flag==0):
    print("false")
else:
    print("true")
   
    