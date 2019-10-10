from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

html = urlopen("https://baike.baidu.com/item/Python/407313").read().decode('utf-8')

# res = re.findall(r"<title>(.+?)</title>", html)
# print("\nPage title is: ", res[0])

# soup = BeautifulSoup(html, features='lxml')
# result = soup.findAll("li", {"class" : "month"})
# for r in result:
#   print(r.get_text())


# 爬取百度百科
his = ['/item/%E6%9D%8E%E6%B2%81/7055']
soup = BeautifulSoup(html, features='lxml')
base_url = 'https://baike.baidu.com'
# # 输出每次爬取到的网页
# print(soup.find('h1').get_text(), ' url: ', his[-1])

for i in range(20):
  url = base_url + his[-1]
  html = urlopen(url).read().decode('utf-8')
  soup = BeautifulSoup(html, features='lxml')
  print(soup.find('h1').get_text(), ' url: ', his[-1])
  sub_urls = soup.findAll("a", {'target' : "_blank", "href" : re.compile("/item/(%.{2})+$")})
  if len(sub_urls) != 0 :
    his.append(random.sample(sub_urls, 1)[0]['href'])
  else:
    his.pop();



