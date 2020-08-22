#coding=utf-8
import requests

url = "https://github.com/USER_NAME"
#构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
#构造cookies字典
cookies_str = ""
cookies_dict = {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookies_str.split('; ')}
print(cookies_dict)
response = requests.get(url, headers=headers, cookies=cookies_dict)
print(response.text)