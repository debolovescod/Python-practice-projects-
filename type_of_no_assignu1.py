number = int(input("Enter number: "))

if number > 0:
    print("Positive")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif number < 0:
    print("Negative")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Zero")

