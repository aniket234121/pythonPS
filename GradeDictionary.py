marks={}
total=0
for i in range(4):
    if(i==1):
        marks["math"]=int(input("enter the marks in math: "))
    elif(i==2):
        marks["english"]=int(input("enter the marks in english: "))
    elif(i==3):
        marks["science"]=int(input("enter the marks in science: "))
subjects=list(marks.keys())
for i in subjects:
    total+=int(marks[i])
avg=total/len(marks)
print("average is :",int(avg))
if(avg>80):
    print(' grade is A')
elif(avg>70 and abg<80):
    print('grade is B')
elif(avg>60 and abg<70):
    print('grade is C')
elif(avg>60 and abg<70):
    print('grade is D')