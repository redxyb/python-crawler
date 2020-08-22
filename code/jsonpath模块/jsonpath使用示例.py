#coding=utf-8

book_dict = {
  "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
from jsonpath import jsonpath
#返回列表，如果取不到将返回False
print(jsonpath(book_dict, '$.store..author'))#提取所有的作者'$..author'
print(jsonpath(book_dict, '$.store.book[*].author'))#store中的所有的book的作者
print(jsonpath(book_dict, '$.store.*'))#store下的所有的元素
print(jsonpath(book_dict, '$.store..price'))#store中的所有的内容的价格'$..price'
print(jsonpath(book_dict, '$.store.book[2]'))#第三本书:下标是从0开始的
print(jsonpath(book_dict, '$.store.book[-1:]'))#最后一本书(有错误：'%.store.book[(@.length-1)]')
print(jsonpath(book_dict, '$.store.book[:2]'))#前两本书'$.store.book[0:2]'
print(jsonpath(book_dict, '$.store.book[?(@.isbn)]'))#获取有isbn的所有书
print(jsonpath(book_dict, '$.store.book[?(@.price>10)]'))#获取价值大于10的所有的书
print(jsonpath(book_dict, '$..*'))#获取所有的数据