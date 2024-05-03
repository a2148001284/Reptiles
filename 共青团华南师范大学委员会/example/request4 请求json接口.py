import requests
import json

'''
Json
爬虫不一定整站爬行，还可以请求接口
结构化数据：json，xml
处理方式：直接转化为python类型

大多数手机版的网页可能是json数据
可以在审查元素--network--response看到

有的时候在访问json页面可能发生错误，因为有可能碰到了反爬虫程序，考虑是不是referer缺失等问题
'''
#json在线生成网站:  https://j.tewx.cn/
#http://api.help.bj.cn/apis/aqi3/?id=nanjing
#https://api.help.bj.cn/apis/weather/?id=101060101

#有的接口需要你充值就算了，比如那个天气的，可以换个其他的免费接口

def main():
    url = "https://json.tewx.cn/user/API_kdd531mytfdzm06i?sdAS1dsnuUa3sd=190001&Jsdh4bajs99dii=sohpuisypf4nfaei"
    resp = requests.get(url=url)
    content = resp.content.decode("utf-8")
    print(content)
    print(type(content))
    #把字符串变成了字典
    shuju = json.loads(content)
    print(shuju)
    print(type(shuju))
    #访问json转化后的字典
    #print(shuju["data"]["JSON"]["mydata"]["name"])

    url2="https://api.help.bj.cn/apis/weather/?id=101060101"
    resp2=requests.get(url=url2)
    print(resp2.content)


if __name__ == '__main__':
    main()