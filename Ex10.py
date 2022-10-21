choose = input("Equation? (Y/N)")

if choose == "Y" or "y":
    eq = input("Input an equation:")
    eq = eval(eq)
    print(f"Here's the results:{eq}")

elif choose == "N" or "n":
    def addition (x,y):
        return x+y

    def subtraction (x,y):
        return x-y

    def multiplication (x,y):
        return x*y
    
    def division (x,y):
        return x/y

    x = int(input("Input the first number:"))
    y = int(input("Input the second number:"))
    print("Operation lists:")
    print('"+" as addition')
    print('"-" as subtraction')
    print('"x" as multiplication')
    print('"/" as division')
    z = str(input("Choose the operation:"))

    if z == "+":
        print(f"Here's the results:{addition(x,y)}")
    elif z == "-":
        print(f"Here's the results:{subtraction(x,y)}")
    elif z == "*":
        print(f"Here's the results:{multiplication(x,y)}")
    elif z == "/":
        print(f"Here's the results:{division(x,y)}")
    else:
        print("me still stupid ya cant")
else:
    print("lah kok lain")

    
        