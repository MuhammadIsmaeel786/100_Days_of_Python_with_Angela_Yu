import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

print("Welcome To Hangman Game !!!! \n")

lives = 0
word_list = ["rizwan", "babar", "afridi","faheem","saim"]
chosen_word = random.choice(word_list)
placeholder = ''
for position in range(len(chosen_word)):
    placeholder += '_'
game_over = False
print(placeholder)
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already gussed this word : {guess}")
    display = ''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter      
        else:
            display += '_'
    print(display)

    if guess not in chosen_word:
        lives += 1
        print("You have losed a life Bro Please Play Seriously")
        if lives == 6:
            game_over =True
            print("You Lose !!!")

    if '_' not in display:
        game_over= True
        print("You won")
    
    print(stages[lives])