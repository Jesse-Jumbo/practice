import requests
import json

from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/trending"

response = requests.get(url)

if response.status_code == requests.codes.OK:
    soup = BeautifulSoup(response.text, "html.parser")

# 影片標題與標題的超連結


# 頻道名稱


# 觀看次數


# 發布時間