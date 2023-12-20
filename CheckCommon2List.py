str1 =input("enter the list 1 seprated by spaces");
mylist=str1.split()
str2 =input("enter the list 2 seprated by spaces");
mylist2=str2.split()

def checkCommon(mylist,mylist2):
    common=set(mylist)&set(mylist2)

    return bool(common)

print(checkCommon(mylist,mylist2))