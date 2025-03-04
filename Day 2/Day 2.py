print("Welcome to the Tip Calculator")
total_bill = float(input('What was the total bill? $ '))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_p = tip / 100
each_person_pay = (total_bill*tip_p + total_bill)/people

print(f"Each person should pay: { round(each_person_pay , 2)}" )
