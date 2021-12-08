import requests
import json

from bs4 import BeautifulSoup

url = "https://pttgopolitics.com/hotest/"

response = requests.get(url)

Soup = BeautifulSoup(response.text, 'html.parser')

the_top_20_article = Soup.select(".block-item > .block-item-title > a", limit=20)

the_top_20_ptt_gossip_boards_list = []
for article_hyper_links in the_top_20_article:
    the_top_20_article_hyper_links = requests.get("https://pttgopolitics.com" + article_hyper_links.get('href'))

    soup = BeautifulSoup(the_top_20_article_hyper_links.text, "html.parser")

    the_top_20_articles_data = {"writer": "",  "title": "", "context": "", "IP": "", "post time": "", "comments": ""}
    all_comments = []
    context = ""
    contexts = ""
# 作者(name)
    for the_top_20_articles_writer in soup.select('.author'):
        the_top_20_articles_data["writer"] = the_top_20_articles_writer.text.strip()
# 標題(thread-title)
    for the_top_20_article_title in soup.select('.thread-title'):
        the_top_20_articles_data["title"] = the_top_20_article_title.text.strip()
# 內文(main-content)
    for the_top_20_article_context in soup.find(class_='bbs-content'):
        context += the_top_20_article_context.text.rstrip(the_top_20_article_context.text[the_top_20_article_context.find('-'):]).strip()
        for x in range(len(context)):
            contexts = context.replace("\n", "")
        the_top_20_articles_data["context"] = contexts

# IP位置(f2)
    for the_top_20_articles_writer_ip in soup.find(class_='f2'):
        the_top_20_articles_data["IP"] = the_top_20_articles_writer_ip.text

# 日期(post-time)
    for the_top_20_article_post_time in soup.select('.post-time'):
        the_top_20_articles_data["post time"] = the_top_20_article_post_time.text.strip()

# 留言(push)
    for the_top_20_article_comments in soup.select('.push'):
        all_comments.append(the_top_20_article_comments.text.strip())
        the_top_20_articles_data["comments"] = all_comments

    the_top_20_ptt_gossip_boards_list.append(the_top_20_articles_data)

filename = "the_top_20_ptt_gossip_boards_article.json"

with open(filename, 'w') as w_f:
    article_data = the_top_20_ptt_gossip_boards_list
    w_f.write(json.dumps(article_data,  sort_keys=True, indent=4))

    print(article_data)
