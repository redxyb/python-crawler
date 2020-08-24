from lxml import etree
html_str = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''
html = etree.HTML(html_str)
handle_html_str = etree.tostring(html).decode()#不解码输出的是字节流
print(handle_html_str)#输出一个完整的html格式的字符串，会自动补全缺失的标签