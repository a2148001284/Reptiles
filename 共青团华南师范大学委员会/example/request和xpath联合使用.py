from lxml import etree
import requests

#pip install lxml
#chrome浏览器需要安装一个 Xpath Helper的插件
#具体xpath语法见当前目录下的txt文档

def reptile(url):  #页面内进行爬虫
    url=url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }
    response=requests.get(url=url,headers=headers)
    html_doc=response.content.decode("utf-8")
    # 使用etree去转化html_doc，转化成了一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    #print(html)  <Element html at 0x196d5543140>
    title=html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()")
    picture=html.xpath("//div[@class='lst']/a/img/@data-src")
    print(title)
    print(picture)

#发现下一页的爬虫
def find_next_page(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode("utf-8")
    html = etree.HTML(html_doc)
    next_page = html.xpath("//a[contains(text(),'下一页')]/@href")
    really_next_page = "http://www.4399dmw.com" + next_page[0]
    return really_next_page

def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/"
    while True:
        try:
            print("start url:" + url)
            reptile(url)
            url = find_next_page(url)
        except:
            break
    print("The last page has been finished!")


if __name__ == '__main__':
    main()

