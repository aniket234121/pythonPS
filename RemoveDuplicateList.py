str =input("enter the list seprated by spaces");
mylist=str.split()
result=[]
print(mylist)
distinctElements=set()
for i in mylist:
    if i not in distinctElements:
        distinctElements.add(i)
        result.append(i)

print("list after removing duplicates:\n",result)

