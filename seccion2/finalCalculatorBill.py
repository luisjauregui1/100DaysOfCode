# greetins calculator
print("Welcome to the tip Calculator!")
# ask for the total bill 
bill = float(input("What was the total bill? $"))
# How much tip would you like to give ?  
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# How many people to split the bill? 
people = int(input("How many people to split the bill? "))
# Each person should pay: ?

total_tip_amount = bill * (tip / 100)
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
fina_amount = round(bill_per_person,2)
fina_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${fina_amount}")