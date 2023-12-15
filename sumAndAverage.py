n=int(input("enter no of elements"))
list=[]
for i in range(0,n,1):
    list.append(int(input("enter element")))
   
print("sum of list is : ",sum(list))
print("average of list is :",sum(list)/n)


