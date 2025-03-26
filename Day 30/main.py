#file not Found
# with open("file.txt", "r") as file:
#     file.read()

#Key Error
# a_dictionary = {"name": "Angela"}
# print(a_dictionary["age"])

# IndexError
# fruits = ["apple", "banana", "cherry"]
# print(fruits[3])

# TypeError
# text = "abc"
# print(text + 3)


# try:
#     with open("file.txt", "r") as file:
#         file.read()
# # If there is an error in code
# except FileNotFoundError:
#     print("The file does not exist.")
# # If there is no error in code
# else:
#     print("The file was found.")
# # If there is an error or not
# finally:
#     print("The file was processed.")
#
#
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# if height > 3:
#     raise ValueError("height cannot be greater than 3 meters")
# bmi = weight / height ** 2
# print(bmi)


import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters are allowed")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()