
pair=int(input("enter the no of pair in dictionary"))
dict={}
for j in range(pair):
    key=input("enter key: ")
    value=input("enter value: ")
    dict[key]=value
sum=0
for i in dict:
    sum+=int(dict[i])
print(sum)
