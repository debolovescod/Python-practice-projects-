x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
operator = input("Enter operator: ")

if operator == "+":
    print(x + y)
elif operator == "-":
    print(x - y)
elif operator == "*":
    print(x * y)
elif operator == "/":
    if y == 0:
        print("Cannot divide by zero")
    else:
        print(x / y)
else:
    print("Invalid operator")