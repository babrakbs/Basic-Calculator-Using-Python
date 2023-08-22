print("\t\t\tWELCOME TO PYTHON BASIC CALCULATOR")


def add(num1, num2):
    result = num1+num2
    print("Sum is =", result)


def subtract(num1, num2):
    result = num1-num2
    print("Subtraction will be= ", result)


def multiply(num1, num2):
    result = num1*num2
    print("Multiplication will be= ", result)


def division(num1, num2):
    if num2 == 0:
        print("Math Error [Division with Zero is Not Possible]")
    else:
        result = num1/num2
        print("Division will be= ", result)


def calculation():
    check = True
    while check:
        num1 = float(input("Enter your 1st Number= "))
        num2 = float(input("Enter your 2nd Number= "))
        op = input("Please Enter your Operation (+,-,*,/) = ")
        if op == "+":
            add(num1, num2)
            check = False
        elif op == "-":
            subtract(num1, num2)
            check = False
        elif op == "*":
            multiply(num1, num2)
            check = False
        elif op == "/":
            division(num1, num2)
            check = False

        else:
            print("Enter valid numbers and operator !")


try:
    calculation()


except ValueError:
    print("Invalid Inputs")
    calculation()
