print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#My answer
#tip_per_person = tip / 100 * bill
#total_bill = tip_per_person + bill
#split_per_person = total_bill / people
#print(f"Each person should pay {split_per_person}")

#Angela's answer ver.1
#bill_with_tip = tip / 100 * bill + bill
#print(bill_with_tip)

#Angela's answer ver.2
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")