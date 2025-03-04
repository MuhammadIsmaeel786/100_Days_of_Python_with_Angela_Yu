print("Welcome to Pizza Hut")
size =input("What size pizza do you want S,M,L : ")
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N : ")
if pepperoni == 'Y' and size == 'S':
    bill += 2
elif pepperoni == "Y" and size == "M" or size == "L":
    bill += 3
chesse = input("Do you want extra chesse? Y or N : ")
if chesse == 'Y':
    bill += 1

print(f"Your final Bill is : ${bill}")
