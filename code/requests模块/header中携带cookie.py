#coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Cookie": ""#使用浏览器登录该网页获取
}
url = 'https://github.com/login'
params = {}

response = requests.get(url, headers=headers, timeout=3)#加入超时参数
print(response.content.decode())