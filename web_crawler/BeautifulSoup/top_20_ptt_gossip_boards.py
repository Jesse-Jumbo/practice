import requests
import json

from bs4 import BeautifulSoup
from test_case import *

url = "https://pttgopolitics.com/hotest/"

response = requests.get(url)

Soup = BeautifulSoup(response.text, 'html.parser')

all_article_links = Soup.select(".block-item > .block-item-title > a", limit=2)
the_top_20_ptt_gossip_boards_list = []
for article_link in all_article_links:

    the_article_link = requests.get("https://pttgopolitics.com" + article_link.get('href'))

    soup = BeautifulSoup(the_article_link.text, "html.parser")
    the_articles_data = {"author": "", "title": "", "context": "", "IP": "", "post time": "", "comments": ""}
    the_comment = {"replay": "", "name": "", "comment": "", "IP": "", "time": ""}
    context = ""
    contexts = ""
    text = ""
    text_list = []
    the_context = ""
    all_comments = []

    # 作者(name)
    the_articles_data["author"] = soup.find(class_='author').text.strip()

    # 標題(thread-title)
    the_articles_data["title"] = soup.find(class_='thread-title').text.strip()

    # 內文(main-content)
    for the_article_context in soup.find(class_='bbs-content'):
        context += the_article_context.text.rstrip(the_article_context.text[the_article_context.find('-'):]).strip()
        the_articles_data["context"] = context

    # IP位置(f2)
    the_articles_data["IP"] = ip_location(soup.find(class_='f2').text)

    # 日期(post-time)
    the_articles_data["post time"] = soup.find(class_='post-time').text.strip()

    # 留言
    comments = soup.select('.push')
    for comment in comments:
        # 留言回應(push)
        replay = soup.find('span', {'class': 'push-tag'})
        the_comment["replay"] = replay.text

        # 留言的人
        name = soup.find('span', {'class': 'push-userid'})
        the_comment["name"] = name.text

        # 留言內文
        content = soup.find('span', {'class': 'push-content'})
        the_comment["comment"] = content.text

        # 留言人IP
        IP = soup.find('span', {'class': 'push-ipdatetime'})
        the_comment["IP"] = comments_object_ip(IP.text)

        # 留言時間
        time = soup.find('span', {"class": 'push-ipdatetime'})
        the_comment["time"] = comments_object_time(time.text)

        all_comments.append(the_comment)
    the_articles_data["comments"] = all_comments
    the_top_20_ptt_gossip_boards_list.append(the_articles_data)

filename = "the_top_20_ptt_gossip_boards_article.json"
with open(filename, 'w') as w_f:
    article_data = the_top_20_ptt_gossip_boards_list
    w_f.write(json.dumps(article_data,  sort_keys=True, indent=4))

    print(article_data)

