# -*- coding: utf-8 -*-
# @Project : download
# @File : download
# @IDE：PyCharm
# @Author : KT15
# @Time : 2022/8/12 10:41






import webbrowser as web
import codecs
import time
with open('C:\\Users\\KT15\\Desktop\\666.txt') as fp:
  for ebayno in fp:
    url = ebayno.strip()
    # time.sleep(1)
    # print(url)
    web.open(url)
