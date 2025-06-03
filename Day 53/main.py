from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Part 1 - Scrape the links, addresses, and prices of the rental properties

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Use our Zillow-Clone website (instead of Zillow.com)
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
# Python list comprehension (covered in Day 26)
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings in total: \n")

# Create a list of all the addresses on the page using a CSS Selector
# Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")

# Create a list of all the prices on the page using a CSS Selector
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")


driver = webdriver.Chrome(options=chrome_options)




for i in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdsmnIu3GX4UxoND4cAw9a8bDCMnvyBtozVgnJwQApPFBwZDA/viewform")
    time.sleep(2)
    input_1 = driver.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_2 = driver.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_3 = driver.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_ = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    time.sleep(2)
    input_1.click()
    input_1.send_keys(all_links[i])
    input_2.click()
    input_2.send_keys(all_addresses[i])
    input_3.click()
    input_3.send_keys(all_prices[i])

    submit_.click()
    time.sleep(3)

