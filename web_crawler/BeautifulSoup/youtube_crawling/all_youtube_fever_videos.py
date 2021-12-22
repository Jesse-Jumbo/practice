import requests
import json

from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://www.youtube.com/feed/trending"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(e)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

fever_video = {"href": "", "video title": "", "channel name": "", "views": "", "uploaded": ""}

href_list = []
video_title_list = []
channel_name_list = []
views_list = []
post_time_list = []

# 影片標題與標題的超連結
test = soup.select('body > script > title')
print(test)
    # print(video_title)
    # print(video_title.select('a').get(['title']))
    # video_title_list.append(video_title.select("a[rel='spf-prefetch]"))

    # print(video_title_list[0])

# 頻道名稱


# 觀看次數


# 發布時間