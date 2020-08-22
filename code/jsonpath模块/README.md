# jsonpath模块
解决问题：从一个多层嵌套的复杂字典中，根据key和下标来批量提取value

jsonpath模块提取数据的方法：

    from jsonpath import jsonpath
    ret = jsonpath(a, 'jsonpath语法规则字符串')
   
jsonpath语法规则：

    $：根节点 
    @：现行节点
    . or []：取子节点
    n/a：取父节点，Jsonpath未支持
    ..：就是不管位置，选择所有符合条件的条件
    *：匹配所有元素节点
    []：迭代器标示（可以在里面做简单的迭代操作，如数组下标，根据内容选值等）
    [,]：支持迭代器中做多选
    ?()：支持过滤操作
    ()：支持表达式计算
  
json.loads()：将字符串形式的数据转化为字典

json.dumps()：将字典形式的数据转化为字符串

json.dump()和json.load()来编码和解码JSON数据，用于处理文件。
    
    with open('test.json', 'w') as f:
        json.dump(data, f)
    with open('test.json', 'r') as f:
        data = json.load(f)
