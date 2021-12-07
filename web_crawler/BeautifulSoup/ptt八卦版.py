import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Beauty/index.html"
res = requests.get(url, cookies={'over18': '1'})

Soup = BeautifulSoup(res.text, 'html.parser')

print(Soup.title, "\n", "\n")  # 可以讀取的網頁的title
print(Soup.title.text, "\n", "\n")
print(Soup.title.string, "\n", "\n")

Soup.find(class_='r-ent')  # 找到第一個class為'r-ent'的元素
print(Soup.find(class_='r-ent'), "\n", "\n")

Soup.find(class_='r-ent').find(class_='title')
print(Soup.find(class_='r-ent').find(class_='title'), "\n", "\n")

Soup.find(class_='r-ent').find(class_='title').find('a')
print(Soup.find(class_='r-ent').find(class_='title').find('a'), "\n", "\n")

Soup.find(class_='r-ent').find(class_='title').a  # 語法糖
print(Soup.find(class_='r-ent').find(class_='title').a.text, "\n", "\n")

Soup.find(class_='r-ent').find(class_='title').a.get('href')
print(Soup.find(class_='r-ent').find(class_='title').a.get('href'), "\n", "\n")
# 從a標籤中用.get('屬性名')的方式讀取該屬性的值
Soup.find(class_='r-ent').find(class_='title').a['href']
print(Soup.find(class_='r-ent').find(class_='title').a['href'], "\n", "\n")
# 或是像字典一樣用鍵值的方式，來讀取該屬性的值

Soup.find_all(class_='r-ent')  # 可以找到全部class為'r-ent'的元素
for i in Soup.find_all(class_='r-ent'):
    if i.a == None:
        print(i.find(class_='title'))
        print(i.find(class_='title').text)
        print(i.find(class_='title').a)
        continue
    print(i.find(class_='title').a.text, "\n", "\n")  # 印出標題
    print('https://www.ptt.cc', end='')  # 因為href中的網址不完整，要補上
    print(i.find(class_='title').a['href'], "\n", "\n")  # 然後跟上面的接在一起

Soup.select_one('.r-ent > .title > a ')
print(Soup.select_one('.r-ent > .title > a '), "\n\n")
print(Soup.find(class_='r-ent').find(class_='title').find('a'), "\n\n")

for i in Soup.select('.r-ent > .title > a '):
    print(i.text, "\n\n")                   # 印出標題
    print('https://www.ptt.cc', end='')     # 補上不完整的網址
    print(i['href'], "\n\n")                # 讀出藏在href中的超連結網址
