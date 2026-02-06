memebers = ["Belle", "Deye", "Maya", "Clair", "Sophia"]
new_memeber = input("Enter your name: ")

if new_memeber in memebers:
    print("Welcome, access granted")
else: 
    memebers.append(new_memeber)
    print("You're a new memeber. Welcome")
print(memebers)