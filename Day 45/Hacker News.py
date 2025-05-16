from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("a", class_="storylink")
articles_text = []
article_links = []
for article in articles:
    articles_text.append(article.getText())
    article_links.append(article.get("href"))
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span",class_="score")]

largest_upvote = max(article_upvotes)
index_of_largest_upvote = article_upvotes.index(largest_upvote)

print(articles_text[index_of_largest_upvote])
print(article_links[index_of_largest_upvote])



