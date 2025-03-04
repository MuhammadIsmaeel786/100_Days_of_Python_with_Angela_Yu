# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# print(timmy)
# print(my_screen.canvheight)
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)

from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

# Define columns
table.field_names = ["Pokémon", "Type", "HP", "Attack", "Defense"]

# Add rows
table.add_row(["Pikachu", "Electric", 35, 55, 40])
table.add_row(["Charizard", "Fire/Flying", 78, 84, 78])
table.add_row(["Bulbasaur", "Grass/Poison", 45, 49, 49])
table.add_row(["Squirtle", "Water", 44, 48, 65])
table.add_row(["Gengar", "Ghost/Poison", 60, 65, 60])
# Print table
print(table)
