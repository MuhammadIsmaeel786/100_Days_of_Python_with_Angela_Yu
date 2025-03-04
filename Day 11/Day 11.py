import random
logo = """
.------.          _     _            _    _            _    
|A_  _ |.        | |   | |          | |  (_)          | |   
|( \/ ).-----.   | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |   | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |   | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |   |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                          _/ |                
      `------'                         |__/           
"""


def deal_cards():
    # Returns a Random card
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "Win, you have Blackjack!"
    elif u_score > 21:
        return "Lose, you went over 21!"
    elif c_score > 21:
        return "Win, opponent went over 21!"
    elif u_score > c_score:
        return "Win, you have a higher score than the opponent."
    else:
        return "Lose, the opponent has a higher score than you."

def play_game():
    print(logo)
    computer_cards = []
    user_cards = []
    user_score = -1
    computer_score = -1

    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        # Display final hands, scores and results
        print(f"\nYour final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Player decision to draw another card
            user_should_deal = input("Do you want to draw another card? Type 'y' or 'n': ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)




    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(f'Computer final hand: {computer_cards}, final score: {computer_score}')
    print(compare(user_score,computer_score))
while input("Do you wanna Play Again a New Game of Black Jack 'y' or 'n' : ") == "y":
    print('\n'*20)
    play_game()
