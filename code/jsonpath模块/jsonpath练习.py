#coding=utf-8
import requests, json
from jsonpath import jsonpath

#获取拉钩网城市json字符串
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
resp = requests.get(url, headers=headers)
html_str = resp.content.decode()
# print(html_str)

#把json格式字符串转化成python对象
jsonobj = json.loads(html_str)#将字符串形式的数据转化为字典
# print(type(jsonobj))#dict
citylist = jsonpath(jsonobj, '$..name')
# print(type(citylist))#list
with open('cities_name.txt', 'w') as file:
    # content = json.dumps(citylist, ensure_ascii=False)#将字典形式的数据转化为字符串
    # print(type(content))#str
    for city in citylist:
        file.write(city + '\n')