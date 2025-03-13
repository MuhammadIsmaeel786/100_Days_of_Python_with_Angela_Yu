# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratue = []
#     for row in data:
#         if row[1] != "temp":
#             tempratue.append(int(row[1]))
#

# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# print(data["temp"].max())
# print(data["temp"].mean())

# Get data in Col
# print(data["temp"])
# print(data.temp)

#Get data in Row
# data_row = data[data.day == "Monday"]
# data_row_temp = data[data.temp == data.temp.max()]
# print(data_row_temp)
#
# monday = data[data.day == "Monday"]
# monday_temp = monday[ "temp"][0]
# monday_temp_f = (monday_temp * 9/5) + 32
# print(monday_temp_f)

#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pd.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")
# print(new_data)


import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250314.csv")
num_greys = len(data[data["Primary Fur Color"] == "Gray"])
num_cin = len(data[data["Primary Fur Color"] == "Gray"])
num_black = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_greys, num_cin, num_black]
}

df = pd.DataFrame(data_dict)
df.to_csv("fur_color.csv")
print(df)