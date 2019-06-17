# -*- coding=UTF-8 -*-

import sys
import io
from urllib import request
from lxml import etree
import json
import requests
import time

# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 登录后才能访问的网页
url = 'https://dasai.ruc.edu.cn/index.php/clubSite/xWork'
# 浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'PHPSESSID=1v2b70ileou4ep8he4d51hasf5'

req = request.Request(url)
# 设置cookie
req.add_header('cookie', cookie_str)
# 设置请求头
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')

# 获取编号
resp = request.urlopen(req)
HTML = etree.HTML(resp.read().decode('utf-8'))
IDs = HTML.xpath( '//div[@class="workList"]/div[@class="block"]/input[@class="workId"]/@value')
print(IDs)

dict = []
inum = 0
for id in IDs:
    # baseUrl = "https://dasai.ruc.edu.cn/index.php/clubSite/xWorkEdit?w=【序号】&c=125#bushu"
    # realUrl = baseUrl.replace("【序号】",str(id))

    # print(realUrl)
    # req = request.Request(realUrl)

    # 设置cookie
    # req.add_header('cookie', cookie_str)
    # 设置请求头
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    # resp = request.urlopen(req)

    # print(resp.read().decode('utf-8'))
    # HTML = etree.HTML(req.read().decode('utf-8'))
    #print(HTML.xpath('//div//text()'))


    HEADER = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "12",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "自己去找自己学校的Cookie哈~",
        "Host": "dasai.ruc.edu.cn",
        "Origin": "https://dasai.ruc.edu.cn",
        "Referer": "https://dasai.ruc.edu.cn/index.php/clubSite/xWorkEdit?w="+ str(id) +"&c=73",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    post_data = {
        "workId": str(id)
    }
    # print(post_data)
    RES = requests.post("https://dasai.ruc.edu.cn/index.php/competitor/getWork",data=post_data,headers=HEADER)
    import chardet

    # print(chardet.detect(RES.text.encode()))
    result = RES.text.encode('raw_unicode_escape').decode()
    result = json.loads(result)
    # print(RES.text.encode('raw_unicode_escape').decode())
    if(result["workTitle"] != None):
        print(str(result))
        dict.append(result)
        inum = inum + 1
    time.sleep(0.5)
f = open("index.json", "a+",encoding="utf-8")
for i in dict:
    f.write(str(i)+"\r\n")
f.close()
print(inum)
