#coding=utf-8
import requests

# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}

#定义url
# url = 'http://www.fyzb8.com/zhibo.php?id=NBA'
url = 'http://www.fyzb8.com/zhibo.php?'
#请求参数
kw = {'id': 'CBA'}

#发送请求，获取响应
response = requests.get(url, headers=headers, params=kw)

print(response.content.decode('gbk'))