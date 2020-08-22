#coding=utf-8
import requests

#定义目标url
url = 'http://www.fyzb8.com/zhibo.php?id=NBA'

#项目标url发送请求
response = requests.get(url)

#打印响应对象
content = response.content#bytes
print(type(content.decode('gbk')))#str
text = response.text#str
# print(content.decode('gbk'))
# print(text)
#将响应文件写入文本
with open('1.txt', 'w')as file:
    file.write(content.decode('gbk'))#解决中文软码

cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies_dict)
print(response.url)
print(response.headers)#请求头
print(response.status_code)#响应状态码
print(response.cookies)#响应的cookies
print(response.request._cookies)
# print(response.json())
