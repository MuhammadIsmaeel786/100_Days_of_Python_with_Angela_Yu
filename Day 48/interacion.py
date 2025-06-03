from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


# no_articles = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")
# no_articles[1].click()

# Find an element by the link text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Clicking the toggle Search icon
# search_icon = driver.find_element(By.CLASS_NAME, value="search-toggle")
# search_icon.click()
# Find the 'Search' <input> by Name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Muhammad")
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Ismaeel")
email_ = driver.find_element(By.NAME, value="email")
email_.send_keys("ismaeel@python.org")
submit = driver.find_element(By.CLASS_NAME, value="btn")
submit.send_keys(Keys.ENTER)