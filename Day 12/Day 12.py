import random
logo="""
___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/          \/        \//_____/   

"""
print(logo)
print("Welcome to the Number Guessing Game !!! ")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. 'easy' or 'hard' : ").lower()
no_attempts = 0
if difficulty == "easy":
    no_attempts = 10
elif difficulty == "hard":
    no_attempts = 5
else:
    print("Invalid choice. Please choose 'easy' or 'hard' ")

print(f"You have {no_attempts} attempts remaining to guess the Number. ")
number_to_guess = random.randint(1, 100)
while no_attempts > 0: 
    guess = int(input("Make a guess: "))
    if guess == number_to_guess:
        print(f"Yay, You have guessed the number {number_to_guess}")
        no_attempts = 0 
    else:
        no_attempts -= 1
        print(f"Oops, You have {no_attempts} attempts remaining to guess the Number. ")
        if no_attempts == 0:
            print(f"Game Over, The number was {number_to_guess}")
                                                                    