"""
爬虫
"""

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
url = r"https://blog.csdn.net/weixin_30596165/article/details/97770008"
print(url)
res = requests.get(url, headers=headers)
print(res.text)