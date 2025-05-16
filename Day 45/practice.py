from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
print(soup.prettify())

all_a_tags = soup.find_all(name = 'a')

for tag in all_a_tags:
    print(tag.getText())
    print(tag.get('href'))

headings = soup.find_all(name = 'h1',id = 'name')
print(headings)

section_heading = soup.find(name = 'h3', class_ = 'heading')
print(section_heading)

name = soup.select_one('#name')
print(name)

heading = soup.select('.heading')
print(heading)