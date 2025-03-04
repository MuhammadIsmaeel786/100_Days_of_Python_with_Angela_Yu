logo = """           
 .o88b.  .d8b.  d88888b .d8888.  .d8b.  d8888b.  
d8P  Y8 d8' `8b 88'     88'  YP d8' `8b 88  `8D  
8P      88ooo88 88ooooo `8bo.   88ooo88 88oobY'  
8b      88~~~88 88~~~~~   `Y8b. 88~~~88 88`8b    
Y8b  d8 88   88 88.     db   8D 88   88 88 `88.  
 `Y88P' YP   YP Y88888P `8888Y' YP   YP 88   YD  
                                                 
 .o88b. d888888b d8888b. db   db d88888b d8888b. 
d8P  Y8   `88'   88  `8D 88   88 88'     88  `8D 
8P         88    88oodD' 88ooo88 88ooooo 88oobY' 
8b         88    88~~~   88~~~88 88~~~~~ 88`8b   
Y8b  d8   .88.   88      88   88 88.     88 `88. 
 `Y88P' Y888888P 88      YP   YP Y88888P 88   YD 
"""

print(logo)

# Define the two_alphabets list
# Contains duplicates for wrapping around
two_alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# Main loop to keep the program running
while True:
    # Get the operation type (encode/decode) from the user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Get the message to encode/decode
    text = input("\nType your message:\n").lower()
    # Get the shift number for Caesar cipher
    shift = int(input("\nType the shift number:\n"))

    # Define the Caesar cipher function
    def caesar(text, shift, direction):
        # Handling encryption
        if direction == "encode":
            cipher_text = ""
            for letter in text:
                position = two_alphabets.index(letter)
                new_position = position + shift
                new_letter = two_alphabets[new_position % 52]
                cipher_text += new_letter
            print(f"The encoded text is: {cipher_text}")
        # Handling decryption
        elif direction == "decode":
            decoded_text = ""
            for letter in text:
                position = two_alphabets.index(letter)
                # Wrap around two_alphabets
                old_position = (position - shift) % 52
                decoded_text += two_alphabets[old_position]
            print(f"\nThe decoded text is {decoded_text}")
        else:
            print("\nWrong input")

    # Call the Caesar cipher function
    caesar(text, shift, direction)

    # Check if the user wants to restart the process
    restart = input(
        "\nType 'yes' if you want to go again. Otherwise type 'no':\n"
    ).lower()
    # Exit the loop if user types 'no'
    if restart == "no":
        print("\nClosing Caesar Cipher")
        break