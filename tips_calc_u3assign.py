def calculate_tip(bill_amount, tip_perecentage):
   tip = bill_amount *( tip_perecentage/100)
   return tip

try:
    bill = float(input("Enter bill amount:"))
    percent = 15
    result = calculate_tip(bill, percent)
    print(f"The tip will be ${result:.2f}")

except ValueError:
    print("Please enter a valid number")