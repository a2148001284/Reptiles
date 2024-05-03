import requests
import json
from pprint import pprint  #美化打印

'''
#https://www.onlinedatagenerator.com/ 在线数据生成器
#将生成的json数据放到www目录下  http://127.0.0.1/test1.json
'''

'''
1.JSON数据的加载
def main():
    url1="http://127.0.0.1/test1.json"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Referer":"http://www.baidu.com"
    }
    response=requests.get(url=url1,headers=headers)
    json_str=response.content.decode("utf-8")
    #print(json_str)
    ret1=json.loads(json_str)  #转化成字典
    #print(ret1)
    #print(ret1['objects'][4]['EmailAddress'])  # 4指向的是第五个人
    #pprint(ret1)  #美化打印

2.JSON数据的保存
    #保存JSON数据到abc.txt
    #ensure_ascii 可以显示中文
    #indent=2会把子节点向后移动两个空格 看起来更人性化
    with open("abc.txt","w",encoding="utf-8") as f:
        f.write(json.dumps(ret1,ensure_ascii=False,indent=2))
        
3.JSON数据的读取
    with open("abc.txt","r",encoding="utf-8") as f:
        ret2=json.load(f)
        print(ret2)
        print(ret2['objects'])
'''

def main():
    url1="http://127.0.0.1/test1.json"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Referer":"http://www.baidu.com"
    }
    response=requests.get(url=url1,headers=headers)
    json_str=response.content.decode("utf-8")
    ret1=json.loads(json_str)  #转化成字典






if __name__ == '__main__':
    main()