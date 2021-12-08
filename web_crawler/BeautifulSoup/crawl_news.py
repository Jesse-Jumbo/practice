import json

import requests

from bs4 import BeautifulSoup

# 網站首頁
from web_crawler.BeautifulSoup.test_crawl_news import parse_reporter_name

response = requests.get(
    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/"
)

if(response.status_code == requests.codes.ok):
    # 獲取HTML
    soup = BeautifulSoup(response.text, "html.parser")

news_hyperlinks = soup.select('.box_0 > h3 > a')
save_news = []
for every_news_hyperlink in news_hyperlinks:
    news_data = {"pob_date": "", "title": "", "context": "", "reporter": ""}
    context = []
    the_news = requests.get(every_news_hyperlink.get('href'))
    soup = BeautifulSoup(the_news.text, "html.parser")
    for pob_date in soup.select('time'):
        # print(pob_date.text)
        news_data["pob_date"] = pob_date.text.strip()
    for title in soup.select('title'):
        # print(title.text)
        news_data["title"] = title.text
    for p in soup.select('.story > p'):
        # print(p.text)
        if p.select('img'):
            context.append("https:" + p.find('img').get('src'))
            continue
        context.append(p.text.strip())
        news_data["context"] = context
    for reporter in soup.select('.story > p')[2:3]:
        # print(reporter.get_text())
        news_data["reporter"] = parse_reporter_name(reporter.text)

    save_news.append(news_data)

filename = "select_all_news.json"

with open(filename, 'w') as w_f:
    update_news = save_news
    json.dump(update_news, w_f)
    print(update_news)
