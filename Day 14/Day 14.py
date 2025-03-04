from game_data_day_14 import data
import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(logo)


def data_to_be_compared():
    random_selection = random.randint(0,len(data)-1)
    name =  data[random_selection]['name']
    follower = data[random_selection]['follower_count']
    description = data[random_selection]['description']
    country = data[random_selection]['country']
    return {"Name" : name, "Followers": follower,"Description": description, "Country": country}

a = data_to_be_compared()
b = data_to_be_compared()
score = 0
game_over = True

while game_over:
    if a['Followers'] == b['Followers']:
        b = data_to_be_compared()
    else:
        print(f"Comaper A : {a['Name']} a {a['Description']}, from {a['Country']}")
        print(vs)
        print(f"Against : {b['Name']} a {b['Description']}, from {b['Country']}")

        followers_c =  input("Who has more followers Type 'A' or 'B' : ").lower()
        if followers_c == 'a':
            if a['Followers'] > b['Followers']:
                a = b
                b = data_to_be_compared()
                score+=1
            else:
                print(f"Sorry You Guessed it Totally Wrong your Score is {score} !!!")
                game_over = False
        elif followers_c == 'b':
            if b['Followers'] > a['Followers']:
                a = b
                b = data_to_be_compared()
                score+=1
            else:
                print(f"Sorry You Guessed it Totally Wrong your Score is {score} !!!")
                game_over = False
        else:
            print("Invalid input")

        if score > 5:
            print("But You are Intelligent")