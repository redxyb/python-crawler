# lxml模块
lxml模块可以利用XPath规则语法，来快速的定位HTML\XML文档中特定元素及获取节点信息（文本内容、属性值）

XPath(XML Path Language)是一门在HTML\XML文档中查找信息的语言，可用来在HTML\XML文档中对**元素和属性进行遍历**。

提取xml、html中的数据需要lxml模块和xpath语法配合使用

1.xpath的节点关系
    xpath中的节点是什么？
    
    每个html、xml的标签都是节点，其中最顶层的节点成为根节点
   
2.xpath定位节点以及提取属性或文本内容的语法

    nodename：选中该元素
    /：从根节点选取、或者是元素和时间的过渡
    //：从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
    .：选取当前节点
    ..：选取当前节点的父节点
    @：选取属性
    text()：选取文本
    
3.xpath节点修饰语法

示例：

    路径表达式                           结果
    //tilte[@lang="eng"]                选择lang属性值为eng的所有title元素
    /bookstore/book[1]                  选择属于bookstore子元素的第一个book元素
    /bookstore/book[last()]             选取属于bookstore子元素的最后一个book元素
    /bookstore/book[last()-1]           选取属于 bookstore 子元素的倒数第二个 book 元素
    /bookstore/book[position()>1]       选择bookstore下面的book元素，从第二个开始选择
    //book/title[text()='Harry Potter'] 选择所有book下的title元素，仅仅选择文本为Harry Potter的title元素
    /bookstore/book[price>35.00]/title  选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00
    
关于xpath的下标：第一个元素的位置是1，最后一个元素的位置是last()，倒数第二个元素的位置是last()-1

xpath其他常用节点选择语法

4.可以通过通配符来选取未知的html、xml的元素
    
    通配符             描述
    *                 匹配任何元素节点
    node()            匹配任何类型的节点
   例如：  //*：选中全部的标签
          //node()：选中全部的属性
          
5.lxml模块的使用

   1.导入lxml的etree库
        
        from lxml import etree
        
   2.利用etree.HTML，将html字符串（bytes类型或str类型）转化为Element对象，Element对象具有xpath的方法，返回结果的列表
    
        html = etree.HTML(text)
        ret_list = html.xpath("xpath语法规则字符串")
       
   3.xpath方法返回列表的三种情况
   
        返回空列表：根据xpath语法规则字符串，没有定位到任何元素
        返回又字符串构成的列表：xpath字符串规则匹配的一定是文本内容或某属性的值
        返回又Element对象构成的列表：xpath规则字符串匹配的是标签，列表中的Element对象可以继续进行xpath
        
6.lxml模块中的etree.tostring函数的使用
    
    from lxml import etree
    html_str = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''
    html = etree.HTML(html_str)
    handeled_html_str = etree.tostring(html).decode()
    print(handeled_html_str)

   输出结果：

    <html><body><div> <ul> 
    <li class="item-1"><a href="link1.html">first item</a></li> 
    <li class="item-1"><a href="link2.html">second item</a></li> 
    <li class="item-inactive"><a href="link3.html">third item</a></li> 
    <li class="item-1"><a href="link4.html">fourth item</a></li> 
    <li class="item-0"><a href="link5.html">fifth item</a> 
    </li></ul> </div> </body></html>

输出的内容：会将字符串中缺失的html标签补全完整，生成一个完整的html格式的字符串

总结：
    
    lxml.etree.HTML(html_str)可以自动补全标签
    lxml.etree.tostring函数可以将转换为Element对象再转回html字符串
    爬虫如果使用lxml来提取数据，应该以lxml.etree.tostring的返回结果作为提取对象
    