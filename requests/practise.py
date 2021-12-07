import requests

# GET 請求
r = requests.get('https://www.google.com.tw/')
print(r.status_code)
# 驗證
if r.status_code == requests.codes.ok:
    print("OK")
# HTML原始碼
print(r.text)

# 增加URL查詢參數
my_params = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=my_params)
print(r.url)

# 自訂請求表頭
my_headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('http://httpbin.org/get', headers=my_headers)

# 帳號密碼登入
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

# POST 請求
my_data = {'key1': 'value1', 'key2': 'value2'}
# 具有重複鍵值的資料
my_data2 = ({'key1': 'value1'}, {'key1': 'value2'})
r = requests.post('http://httpbin.org/post', data=my_data)

# 上傳檔案
my_files = {'my_filename': open('my_file.docx', 'rb')}
r = requests.post('https://httpbin.org/post', files=my_files)

# Cookie
r = requests.get("http://my.server.com/has/cookies")
print(r.cookies['my_cookie_name'])

my_cookies = dict(my_cookie_name='G. T. Wang')
r = requests.get("https://httpbin.org/cookies", cookies=my_cookies)

# 等待逾時
requests.get('http://github.com/', timeout=3)   # 秒

# 不合格憑證
r = requests.get('https://my.server.com/', verify=False)    # 關閉憑證檢查