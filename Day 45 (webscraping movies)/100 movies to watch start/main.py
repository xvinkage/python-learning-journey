import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify)

movies = []
titles = soup.select(selector="h3.title")
for title in titles:
    title_text = title.getText()
    movies.append(title_text)
movies.reverse()

with open("movies.txt", "w", encoding="utf-8") as movie_file:
    for movie in movies:
        movie_file.write(f"{movie}\n")

# print(movies)

