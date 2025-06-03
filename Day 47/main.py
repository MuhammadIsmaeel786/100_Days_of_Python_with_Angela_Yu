from bs4 import BeautifulSoup
import requests
import smtplib

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
           "Accept-Language":"en-US,en;q=0.9",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, br, zstd",
           "Dnt": "1",
           "Priority": "u=1",
           "Sec-Fetch-Dest": "document",
           "Sec-Fetch-Mode": "navigate",
           "Sec-Fetch-Site": "none",
           "Sec-Fetch-User": "?1",
           "Sec-Gpc": "1",
           "Upgrade-Insecure-Requests": "1",
           }
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
# Find the HTML element that contains the price
price = soup.find_all("span", class_="a-price-whole")[0].get_text().strip('.')

# Convert to floating point number
price_as_float = float(price)

# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").get_text().strip()


# Set the price below which you would like to get a notification
BUY_PRICE = 80
#
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com","587") as connection:
        connection.starttls()
        result = connection.login("muhammadismaeelsaghar@gmail.com", "gjfj csqr ujro jklo")
        connection.sendmail(
            from_addr="muhammadismaeelsaghar@gmail.com",
            to_addrs='isaghar61@gmail.com',
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )