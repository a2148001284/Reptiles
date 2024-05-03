import requests
''' 1.普通读取网页源代码内容
def main():
    url="https://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.85.400 QQBrowser/10.9.4610.400"
    }
    resp=requests.get(url=url,headers=headers)
    with open("a.txt","wb+") as f:
        f.write(resp.content)  #写入文件
'''

'''2.批量保存网页源代码中的内容
def main():
    url = "https://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.85.400 QQBrowser/10.9.4610.400"
    }
    for i in range(14):
        urla=url.format(i)
        print(urla)
        resp = requests.get(url=urla, headers=headers)
        with open("a"+str(i)+".txt","wb+") as f:
            #写入文件
            f.write(resp.content)
'''

'''
爬虫小知识：
1.代理使用的目的 
(1)可能是国外的网站 
(2)同时别人的网站可能存在反爬虫装置 访问过多ip会被屏蔽  代理也就是一种反反爬虫的手段 
(3)可以防止自己的ip泄露或者被追踪
代理网站:
快代理  https://www.kuaidaili.com/
'''
#增加代理的方式:
#proxies = {"HTTP":"http://123.169.122.201:9999"}
#resp = requests.get(url=urla,headers=headers,proxies=proxies)
#如果你使用socks系列的代理
#proxies = {"https":"socks5://123.169.122.201:9999"}

#代理类型 http https socket4 socket5
#匿名代理：知道你用代理，但是不知道你是谁
#混淆代理：知道你用代理，但是获取到的是假的ip地址
#高匿代理：无法发现你在使用代理

'''
反爬虫侦测：
(1)一段时间内ip访问频率
(2)检查cookie，session，user-agent，referer，header等参数
(3)服务器提供商
(4)需要ip地址池更新
'''


'''3.处理session（用户登录维持）  
    通过网页的表单知道post的信息，但是网站内部的情况需要登陆之后带着cookie/session信息才能访问
def main():
    url = "http://127.0.0.1/sqli-labs/Less-20/index.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.85.400 QQBrowser/10.9.4610.400"
    }
    data = {"uname":"admin", "passwd":"admin"}
    # 实例化session
    session = requests.session()

    # 发送post请求，提交用户名密码
    session.post(url, headers=headers, data=data)
    #resp=session.post(url,headers=headers,data=data)
    #print(resp.content.decode('utf-8'))  发现已经登录成功 回包是一个已经登录以后的网页

    # 此时session里面已经有cookie的信息了，可以直接用session去get登录后的任何页面
    res = session.get(url, headers=headers)
    print(res.content.decode("utf-8"))
'''


'''4.处理cookie直接登录的情况 直接通过cookie登录 而不需要再传账号密码
    直接带着cookie请求
方法1：
def main():
    url = "http://127.0.0.1/sqli-labs/Less-20/index.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.85.400 QQBrowser/10.9.4610.400"
    }
    cookie_dict = {"uname": "admin"}
    resp = requests.get(url, headers=headers, cookies=cookie_dict)
    print(resp.content.decode("utf-8"))
    

方法2: 把cookie放到headers中即可  
def main():
    url = "http://127.0.0.1/sqli-labs/Less-20/index.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.85.400 QQBrowser/10.9.4610.400",
        "Cookie":"uname = admin"
    }
    resp = requests.get(url, headers=headers)
    print(resp.content.decode("utf-8"))
'''

'''5.正常登录 直接从返回中解码获得cookie信息
def main():
    url = "http://127.0.0.1/sqli-labs/Less-20/index.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.85.400 QQBrowser/10.9.4610.400"
    }
    data = {"uname":"admin", "passwd":"admin"}
    resp=requests.post(url,headers=headers,data=data)
    # 解码cookie
    cookies = requests.utils.dict_from_cookiejar(resp.cookies)
    print(cookies)
'''

#如果要处理https网页  有可能会出现ssl证书问题
#不去验证ssl证书 增加一个verify就可以不去验证证书
#resp = requests.get(url,headers=headers,data=data,verify=False)

#超时参数 timeout
#如果有些网站没有办法爬到 比较慢等情况
#设置3秒钟没反应，如果结合代理去使用的，代理一段时间没反应，就可以从ip池里删除了
#resp = requests.get(url,headers=headers,data=data,verify=False,timeout=3)

#request处理状态码
r=request.get(url,timeout=30)
r.raise_for_status()
#能够判断返回的Response类型状态是不是200。如果是200，他将表示返回的内容是正确的，如果不是200，他就会产生一个HttpError的异常

#Python2的代码：
import requests
code=requests.get("https://www.jb51.net").status_code
print code

import urllib
status=urllib.urlopen("https://www.jb51.net").code
print status

import requests
code=requests.get("https://www.jb51.net").status_code
print code

#python3的代码：
url = request = urllib.request.Request(url,=gHeads)
code = urllib.request.urlopen(request).getcode()


if __name__ == '__main__':
    main()