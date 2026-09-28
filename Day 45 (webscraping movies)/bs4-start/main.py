from bs4 import BeautifulSoup
import requests 

url = "https://news.ycombinator.com/"

response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, "html.parser")

article_li = []

anchors = soup.find_all(name="span", class_="titleline")
for anchor in anchors:
    text = anchor.getText()
    article_li.append(text)

link_li = []
links_text = soup.select(selector="span.titleline > a")
for link in links_text:
    links = link.get("href")
    link_li.append(links)

upvote_li = []
upvote = soup.find_all(name="span", class_="score")
for vote in upvote:
    upvote_text = vote.getText()
    number = int(upvote_text.split()[0])
    upvote_li.append(number)

max_vote = max(upvote_li)

vote_index = upvote_li.index(max_vote)

print(f"Article: {article_li[vote_index]}\nlink: {link_li[vote_index]}\nupvotes: {upvote_li[vote_index]}")
# print(link_li)

# for anchor in anchors:
#     text = anchor.getText()
#     link = 
#     upvote =
#     print(f"text: {text}\nlink: {link}\nupvotes: {upvote}")

# with open("./bs4-start/website.html") as site:
#     content = site.read()

# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title.string)
# # print(soup.p)
# # tags = soup.find_all(name="a")

# # for tag in tags:
# #     print(tag.getText())
# #     print(tag.get("href"))

# # heading = soup.find(name="h1", id="name")
# # print(heading.string)

# # heading2 = soup.find(name="h3", class_="heading")
# # print(heading2)

# name = soup. select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)