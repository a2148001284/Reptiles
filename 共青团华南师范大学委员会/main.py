
import requests
from lxml import etree
import urllib


def GetContent(url):
    url=url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    response = requests.get(url=url, headers=headers)
    html_doc = response.content.decode("utf-8")
    html = etree.HTML(html_doc)
    title=html.xpath("//div[@class='article-title']/h2/text()")
    print(title[0])
    body=html.xpath("//div[@class='article-content']/p/span/text()")
    for i in range(len(body)):
        print(body[i])


#对应于七个大抬头的内容
def GetUrlOf1(url):
    second_url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    response = requests.get(url=second_url, headers=headers)
    html_doc = response.content.decode("utf-8")
    html = etree.HTML(html_doc)
    if(url == "http://youth.scnu.edu.cn/TWJS/"):
        left_title=html.xpath("//ul[@class='cl']/li/a/text()")
        left_url=html.xpath("//ul[@class='cl']/li/a/@href")
        for i in range(len(left_url)):
            #print(left_title[i]+":"+left_content[i])
            #由于最后一个页面没有内容 所以会出现报错 这里可以使用try catch的方法进行捕获 然后直接continue就可以
            GetContent(left_url[i])
            print("-------------------------")
    else:
        left_title = html.xpath("//div[@class='side-menu']//li/a/text()")
        left_url = html.xpath("//div[@class='side-menu']//li/a/@href")
        for i in range(len(left_url)):
            GetUrlOf2(left_url[i])


def GetUrlOf2(url):
    third_url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    response = requests.get(url=third_url, headers=headers)
    html_doc = response.content.decode("utf-8")
    html = etree.HTML(html_doc)
    body_content=html.xpath("//div[@class='category-list']//li/a/text()")
    body_url=html.xpath("//div[@class='category-list']//li/a/@href")
    for i in range(len(body_url)):
        print("--------------"+body_content[i]+"------------")
        GetContent(body_url[i])
    i=2




def main():
    #GetContent("http://youth.scnu.edu.cn/a/20220427/17565.html")
    first_url = "http://youth.scnu.edu.cn/TWJS/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    response = requests.get(url=first_url, headers=headers)
    html_doc = response.content.decode("utf-8")
    html = etree.HTML(html_doc)
    first_title=html.xpath("//div[@id='nv']//li//span/text()")
    first_url=html.xpath("//div[@id='nv']//li/a/@href")
    for i in range(len(first_title)):
        print(first_title[i]+":"+first_url[i+1])







if __name__ == '__main__':
    #main()
    #GetUrlOf1("http://youth.scnu.edu.cn/TWJS/")
    #GetUrlOf2("http://youth.scnu.edu.cn/SXYL/")