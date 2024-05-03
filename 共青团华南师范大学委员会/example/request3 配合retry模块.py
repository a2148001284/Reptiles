import requests
from retrying import retry
#pip install retrying

#如果失败就请求3次，执行3次如果还失败就报错，可以配合try
@retry(stop_max_attempt_number=3)
def ask(inurl):
    url = inurl
    print("开始请求网站")
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.85.400 QQBrowser/10.9.4610.400"
    }
    res = requests.get(url=url,headers=headers,timeout=2)
    with open("c.txt","wb+") as f:
        f.write(res.content)
    print("请求成功")

def main():
    try:
        ask("http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/")
    except:
        print("ask failed! you have tried more than 3 tiems")
    pass

if __name__ == '__main__':
    main()