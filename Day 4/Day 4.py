import random
rock = '''  
Rock
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
paper
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
scissors
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

options =[rock,paper,scissors]
print("Welcome to your new Game !!!")
print(options[0],options[1],options[2])
user = int(input("Rock = 0, Paper = 1  or Scissors 2 : "))
cpu = random.randint(0,2)
if user == cpu:
    print(options[user])
    print(options[cpu]) 
    print("It's a tie !!")
elif user == 0 and cpu == 1:
    print(options[user])
    print(options[cpu]) 
    print("You Loss !!!!")
elif user == 0 and cpu == 2:
    print(options[user])
    print(options[cpu]) 
    print("You Win !!!")
elif user == 1 and cpu == 2:
    print(options[user])
    print(options[cpu]) 
    print("You Loss !!!!")
elif user == 1 and cpu == 0:
    print(options[user])
    print(options[cpu]) 
    print("You Win  !!!!")
elif user == 2 and cpu == 1:
    print(options[user])
    print(options[cpu]) 
    print("You Win  !!!!")
elif user == 2 and cpu == 0:
    print(options[user])
    print(options[cpu]) 
    print("You Loss  !!!!")
else:
    print("Invalid Input !!!!")