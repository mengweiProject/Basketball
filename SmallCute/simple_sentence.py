"""
获取网页源码中的英语短句
"""

import re
import requests
from time import sleep


with open("source_code.txt", "r", encoding="utf-8") as f:
    html = f.read()

def get_sentence(html):
    reg_for_sentence = r"<td>.*?</td>"
    sent_list = re.findall(reg_for_sentence, html)
    for i in sent_list:
        s = re.sub(r"&nbsp;", "", re.sub(r"<.*?>", "", i))
        if "。" not in s and "[" not in s and len(s) > 0 and "“" not in s and "，" not in s and "(" not in s and "？" not in s:
            # print("this is s:" + s + ">>>")
            # print(type(s))
            with open("result.txt", "a") as f_result:
                f_result.write(s.strip(" ") + "\r")
    with open("result.txt", "a") as f_result:\
        f_result.write("---------------------end----------------------")

def get_source(word):
    for i in range(1, 10):
        url = "http://www.jukuu.com/show-{}-{}.html".format(word, i)
        # print(url)
        sleep(2)
        res = requests.get(url)
        html = res.text
        get_sentence(html)


def get_words_list():
    with open("words_list.txt", "r") as f:
        word_list = f.readlines()
        for i in word_list:
            get_source(i.strip())


if __name__ == '__main__':
    get_words_list()