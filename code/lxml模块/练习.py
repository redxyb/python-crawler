from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''
html = etree.HTML(text)
#提取a标签的文本内容以及链接
li_list = html.xpath("//li[@class='item-1']")
#在每一组中继续进行数据的提取
for li in li_list:
    item = {}
    item['href'] = li.xpath("./a/href")[0] if len(li.xpath("./a/href"))>0 else None
    # print(li.xpath("./a/href"))#[]
    item['title'] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()"))>0 else None
    print(item)