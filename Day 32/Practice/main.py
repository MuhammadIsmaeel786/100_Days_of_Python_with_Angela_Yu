import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
my_email = "muhammadismaeelsaghar@gmail.com"
password = "ekln qvpw nkut emvd"
if weekday == 2:
    with open("quotes.txt","r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,to_addrs="isaghar61@gmail.com",msg=f"Subject:Today's Motivation \n\n {quote}")
