#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

option = input("Do you want Easy Password or Hard 0 and 1 : " )
password = []
password_n = ''
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
if option== '0' or option =='1':
    for i in range(nr_letters):
        password += random.choice(letters)
    for i in range(nr_symbols):
        password += random.choice(symbols)
    for i in range(nr_numbers):
        password += random.choice(numbers)
    if option == '0':
        for word in password:
            password_n += word
        print(f"Your Easy password is : {password_n}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P        
    elif option == '1':
        random.shuffle(password)
        for word in password:
            password_n += word
        print(f"Your Hard password is : {password_n}")
else:
    print("Sorry Invalid Option Try Again !!!")