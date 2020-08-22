#coding=utf-8
import requests

url = "https://www.baidu.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
proxies = {
    "https": "https://111.13.100.91:80",
    "http": "http://61.135.186.80:80",
}
resp = requests.get(url, headers=headers, proxies=proxies, verify=False)
print(resp.content.decode())