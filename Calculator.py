def calculator():
        if(c=="+"):
            print(a+b)
        elif (c=="-"):
            print(a-b)
        elif(c=="*"):
            print(a*b)
        elif(c=="%"):
            print(a%b)
        else:
            print("The function not required")
while True:
    a=int(input("Enter the Frist number:"))
    b=int(input("Enter the second number:"))
    c=input("Enter the operator:")
    calculator()
            
