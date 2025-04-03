##################### Normal Starting Project ######################
import smtplib
from datetime import datetime
from random import randint
import pandas as pd
today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
MY_EMAIL = "muhammadismaeelsaghar@gmail.com"
MY_PASSWORD = "ekln qvpw nkut emvd"
birthdays_dict = {(data_row["month"],data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday \n\n{content}")


