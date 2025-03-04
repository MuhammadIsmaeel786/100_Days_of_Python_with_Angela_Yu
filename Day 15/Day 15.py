logo = '''
   ___       _   _             ,__ __               _                    
  / (_)     | | | |           /|  |  |             | |    o              
 |      __  | | | |  _   _     |  |  |   __,   __  | |        _  _    _  
 |     /  \_|/  |/  |/  |/     |  |  |  /  |  /    |/ \   |  / |/ |  |/  
  \___/\__/ |__/|__/|__/|__/   |  |  |_/\_/|_/\___/|   |_/|_/  |  |_/|__/
            |\  |\                                                       
            |/  |/                                                       
'''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

machine_on = True
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffe: {resources['coffee']}gm")
    
print(logo)
print("\nWelcome to the Coffee Machine!")
while machine_on:
    

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
       report()
    elif user_choice == 'off':
        machine_on = False
    elif user_choice in MENU:
        drink = MENU[user_choice]
        if resources["water"] >= drink["ingredients"]["water"] and resources["milk"] >=  drink["ingredients"]["milk"] and resources["coffee"] >= drink["ingredients"]["coffee"]:
            print(f"Please insert coins. ${drink['cost']:.2f}")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            total_cost = quarters * COIN_VALUES["quarter"] + dimes * COIN_VALUES["dime"] + nickels * COIN_VALUES["nickel"] + pennies * COIN_VALUES["penny"]
            if total_cost >= drink["cost"]:
                resources["water"] -= drink["ingredients"]["water"]
                resources["milk"] -= drink["ingredients"]["milk"]
                resources["coffee"] -= drink["ingredients"]["coffee"]
                resources["money"] += drink["cost"]
                change = total_cost - drink["cost"]
                print(f"Here is ${round(change,2)} in change.")
                print(f"Here is your ☕{user_choice}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Sorry, there is not enough resources to make that drink.")
    else:
        print("Sorry, that's not a valid choice.")