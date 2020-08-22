#coding=utf-8
import requests, json

class King(object):
    def __init__(self, word):
        self.url = "http://fy.iciba.com/ajax.php?a=fy"
        self.word = word
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
        self.post_date = {
            "f": "auto",# 表示被翻译的语言是自动识别
            "t": "auto",# 表示翻译后的语言是自动识别
            "w": self.word# 要翻译的中文字符串
        }

    def get_date(self):
        resp = requests.post(self.url, headers=self.headers, data=self.post_date)
        with open("post.txt", 'wb')as file:
            file.write(resp.content)
        return resp.content

    def parse_date(self, date):
        #将json数据转换成python字典
        dict_date = json.loads(date)

        #从字典中抽取翻译结果
        try:
            print(dict_date['content']['out'])#翻译结果在字典对应的位置
        except:
            print(dict_date['content']['word_mean'][0])

    def run(self):
        data = self.get_date()
        self.parse_date(data)

if __name__ == '__main__':
    while True:
        content = input("请输入要翻译的内容：")
        king = King(content)
        king.run()