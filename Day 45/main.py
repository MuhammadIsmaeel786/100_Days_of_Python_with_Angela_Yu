import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

# Write your code below this line 👇
soup = BeautifulSoup(website_html, "html.parser")
all_movies =  soup.find_all("h3",class_="title")
list_of_movies = [movie.getText() for movie in all_movies]
movies = list_of_movies[::-1]

with open("movies.txt", "w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")