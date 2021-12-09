import requests
import json

from bs4 import BeautifulSoup
from test_case import *

url = "https://pttgopolitics.com/hotest/"

response = requests.get(url)

Soup = BeautifulSoup(response.text, 'html.parser')

all_article_links = Soup.select(".block-item > .block-item-title > a", limit=20)
the_top_20_ptt_gossip_boards_list = []
for article_link in all_article_links:

    the_article_link = requests.get("https://pttgopolitics.com" + article_link.get('href'))

    soup = BeautifulSoup(the_article_link.text, "html.parser")
    the_articles_data = {"author_id": "", "title": "", "context": "", "author_IP": "", "post time": "", "comments": ""}
    the_comment = {"reply": "", "user_id": "", "comment": "", "user_IP": "", "time": ""}
    context = ""
    all_comments = []
    all_reply = []
    all_user_name = []
    all_comment = []
    all_IP = []
    all_time = []

    # 作者(name)
    the_articles_data["author_id"] = soup.find(class_='author').text.strip()

    # 標題(thread-title)
    the_articles_data["title"] = soup.find(class_='thread-title').text.strip()

    # 內文(main-content)
    for the_article_context in soup.find(class_='bbs-content'):
        context += the_article_context.text.rstrip(the_article_context.text[the_article_context.find('-'):]).strip()
        the_articles_data["context"] = context

    # IP位置(f2)
    the_articles_data["author_IP"] = ip_location(soup.find(class_='f2').text)

    # 日期(post-time)
    the_articles_data["post time"] = soup.find(class_='post-time').text.strip()


    # 留言回應(push)
    replys = soup.find_all('span', {'class': 'push-tag'})
    for reply in replys:
        # all_reply.append(reply.text)
        all_reply.append(reply_reset(reply.text))
    # print(all_reply)

    # 留言的人
    user_names = soup.find_all('span', {'class': 'push-userid'})
    for user_id in user_names:
        all_user_name.append(user_id.text)

    # 留言內文
    contents = soup.find_all('span', {'class': 'push-content'})
    for content in contents:
        all_comment.append(context_reset(content.text))

    # 留言人IP
    user_IP = soup.find_all('span', {'class': 'push-ipdatetime'})
    for ip in user_IP:
        all_IP.append(comments_object_ip(ip.text))

    # 留言時間
    times = soup.find_all('span', {"class": 'push-ipdatetime'})
    for time in times:
        all_time.append(comments_object_time(time.text))

    for i in range(len(all_time)):
        # the_comment={}
        the_comment["reply"] = all_reply[i]
        the_comment["user_id"] = all_user_name[i]
        the_comment["comment"] = all_comment[i]
        the_comment["user_IP"] = all_IP[i]
        the_comment["time"] = all_time[i]
        all_comments.append(the_comment.copy())
    the_articles_data["comments"] = all_comments
    the_top_20_ptt_gossip_boards_list.append(the_articles_data)

filename = "the_top_20_ptt_gossip_boards_article.json"
with open(filename, 'w') as w_f:
    article_data = the_top_20_ptt_gossip_boards_list
    w_f.write(json.dumps(article_data,  sort_keys=True, indent=4))

    print(article_data)

