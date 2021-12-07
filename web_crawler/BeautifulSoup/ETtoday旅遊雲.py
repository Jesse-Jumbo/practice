import requests

from bs4 import BeautifulSoup


response = requests.get(
    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/"
)

soup = BeautifulSoup(response.text, "html.parser")

print("輸出排版後的HTML內容\n", soup.prettify())

result = soup.find("h3")
print("只搜尋第一個符合條件的HTML節點\n", result)

result = soup.find_all("h3", itemprop="headline", limit=3)  # 利用關鍵字參數指定其屬性值，限制搜尋的節點數量
print("搜尋網頁中所有符合條件的HTML節點\n", result)

result = soup.find_all(["h3", "p"], limit=2)
print("同時搜尋多個HTML標籤\n", result)

result = soup.find("h3", itemprop="headline")
print("選取節點下的單一個子節點\n", result.select_one("a"))

result = soup.find("div", itemprop="itemListElement")
print("選取節點下的多個子節點\n", result.select("a"))

# 以CSS屬性搜尋節點
titles = soup.find("p", class_="summary")
print("搜尋第一個府和指定的HTML標籤及CSS屬性質的節點\n", titles)

titles = soup.find_all("p", class_="summary", limit=3)
print("搜尋網頁中符合指定的HTML標籤及css屬性值的所有節點\n", titles)

titles = soup.select(".summary", limit=3)
print("如果單純只透過css屬性值來進行HTML節點的搜尋\n", titles)


# 搜尋父節點
result = soup.find("a", itemprop="url")
parents = result.find_parents("h3")
print("從某一個節點向上搜尋\n", parents)


# 搜尋前、後節點
result = soup.find("h3", itemprop="headline")
previous_node = result.find_previous_siblings("a")
print("在同一層級的節點，搜尋前一個節點\n", previous_node)

result = soup.find("h3", itemprop="headline")
next_node = result.find_next_siblings("p")
print("同一層級的節點，搜尋後一個節點\n", next_node)


# 取得屬性值
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").get("href"))


# 取得連結文字
titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").getText())






















