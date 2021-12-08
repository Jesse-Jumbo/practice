import requests

from bs4 import BeautifulSoup

url = "https://pttgopolitics.com/hotest/"

response = requests.get(url)

Soup = BeautifulSoup(response.text, 'html.parser')

# 作者

# 標題

# 內文

# IP位置

# 日期

# 留言