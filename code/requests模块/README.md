# requests模块
response.text和response.content的区别：

	response.text:
		类型：str
		解码类型：requests模块自动根据HTTP头部对响应的编码做出有根据的推测，推测文本的编码
	response.content:
		类型：bytes
		解码类型：没有指定
		
利用decode函数对requests.content解决中文乱码：response.content.decode("GBK")

response响应对象的其他常用属性或方法：

    •response.url响应的url；有时候响应的url和请求的url并不一致
    •response.status_code 响应状态码
    •response.request.headers 响应对应的请求头
    •response.headers 响应头
    •response.request._cookies 响应对应请求的cookie；返回cookieJar类型
    •response.cookies 响应的cookie（经过了set-cookie动作；返回cookieJar类型
    •response.json()自动将json字符串类型的响应内容转换为python对象（dict or list）
cookieJar对象转换为cookies字典的方法：requests.utils.dict_from_cookiejar函数

    cookies_dict = requests.utils.dict_form_cookiejar(response.cookies)

超时参数timeout的使用：一个请求很久没有结果，就会让整个项目的效率变得非常低，这个时候就必须让它在特定时间内返回结果，否则就报错。

	response = requests.get(url, timeout=3)     # 设置超时时间

代理的过程：
1.	代理ip是一个ip，指向的是一个代理服务器
2.	代理服务器能帮我们向目标服务器转发请求
 
正向代理和反向代理

为浏览器或客户端（发送请求的一方）转发请求的，叫做正向代理
	
    浏览器知道最终处理请求的服务器的真实ip地址，例如VPN
	
不为浏览器或客户端（发送请求的一方）转发请求、而是为最终处理请求的服务器转发响应结果的叫做反向代理
	
	浏览器不知道服务器的真实地址，例如nginx


代理ip（代理服务器）的分类
1. 根据代理ip的匿名程度，代理IP可以分为下面三类：
   - 透明代理(Transparent Proxy)：透明代理虽然可以直接“隐藏”你的IP地址，但是还是可以查到你是谁。目标服务器接收到的请求头如下：
         
         REMOTE_ADDR = Proxy IP
         HTTP_VIA = Proxy IP
         HTTP_X_FORWARDED_FOR = Your IP
   - 匿名代理(Anonymous Proxy)：使用匿名代理，别人只能知道你用了代理，无法知道你是谁。目标服务器接收到的请求头如下：
         
         REMOTE_ADDR = proxy IP
         HTTP_VIA = proxy IP
         HTTP_X_FORWARDED_FOR = proxy IP
   - 高匿代理(Elite proxy或High Anonymity Proxy)：高匿代理让别人根本无法发现你是在用代理，所以是最好的选择。毫无疑问使用高匿代理效果最好。目标服务器接收到的请求头如下：
         
         REMOTE_ADDR = Proxy IP
         HTTP_VIA = not determined
         HTTP_X_FORWARDED_FOR = not determined
2. 根据网站所使用的协议不同，需要使用相应协议的代理服务。从代理服务请求使用的协议可以分为：
   - http代理：目标url为http协议
   - https代理：目标url为https协议
   - socks隧道代理（例如socks5代理）等：
     1. socks 代理只是简单地传递数据包，不关心是何种应用协议（FTP、HTTP和HTTPS等）。
     2. socks 代理比http、https代理耗时少。
     3. socks 代理可以转发http和https的请求

proxies代理参数的使用
为了让服务器以为不是同一个客户端在请求；为防止频繁向一个域名发送请求被封ip
用法：

    response = requests.get(url, proxies=proxies)
•	proxies的形式：字典
•	例如：

    proxies = { 
        "http": "http://12.34.56.79:9527", 
        "https": "https://12.34.56.79:9527", 
    }

•	注意：如果proxies字典中包含有多个键值对，发送请求时将按照url地址的协议来选择使用相应的代理ip

使用verify参数忽略CA证书
	为了在代码中能够正常的请求，我们使用verify=False参数，此时requests模块发送请求将不做CA证书的验证：verify参数能够忽略CA证书的认证
	
	import requests
    url = "https://sam.huat.edu.cn:8443/selfservice/" 
    response = requests.get(url,verify=False)

xml：可扩展标记语言，和HTML很像，更专注于传输和存储数据，其焦点是数据内容

html：超文本标记语言，专注于显示数据以及如何更好显示数据


