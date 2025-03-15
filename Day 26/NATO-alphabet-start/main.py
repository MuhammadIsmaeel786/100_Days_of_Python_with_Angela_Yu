# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
user_input = input("Enter a word : ").upper()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_list = [phonetic_dict[letter] for letter in user_input]
print(phonetic_list)