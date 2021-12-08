import requests

from bs4 import BeautifulSoup

url = "https://pttgopolitics.com/hotest/"

response = requests.get(url)

Soup = BeautifulSoup(response.text, 'html.parser')

the_top_20_article = Soup.select(".block-item > .block-item-title > a", limit=20)
for i in the_top_20_article:
    the_top_20_article_hyper_links = requests.get("https://pttgopolitics.com" + i.get('href'))
# 作者(name)

# 標題(thread-title)

# 內文(article-metaline)

# IP位置(f2)

# 日期(post-time)

# 留言(push)