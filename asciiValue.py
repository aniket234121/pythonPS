char=str(input("enter a character to print ascii value: "))
if(len(char)>1):
    print("invalid input")
else:
    print("ASCII value of ",char," is ",ord(char))