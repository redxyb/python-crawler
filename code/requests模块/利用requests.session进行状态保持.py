#coding=utf-8
import requests, re

#构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

#实例化session对象
session = requests.session()

#访问登录页面获取登录请求所需参数
response = requests.get('https://github.com/login', headers=headers)
# print(response.content.decode())
authenticity_token = re.search('name="authenticity_token" value="(.*?)" />', response.text).group(1) # 使用正则获取登陆请求所需参数

# 构造登陆请求参数字典
data = {
    'commit': 'Sign in', # 固定值
    'utf8': '✓', # 固定值
    'authenticity_token': authenticity_token,# 该参数在登陆页的响应内容中
    'login': input('输入github账号：'),
    'password': input('输入github密码：')
}

# 发送登陆请求（无需关注本次请求的响应）
session.post('https://github.com/session', headers=headers, data=data)

# 打印需要登陆后才能访问的页面
response = session.get('https://github.com/redxyb/python-crawler', headers=headers)
print(response.content)
