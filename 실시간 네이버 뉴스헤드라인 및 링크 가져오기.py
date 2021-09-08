# 웹크롤링으로 네이버 뉴스 헤드라인및 해당링크 가져오기

import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today()
print("\n{}년 {}월 {}일 {}시 {}분 \n네이버 뉴스 헤드라인 및 링크\n".format(today.year,today.month,today.day,today.hour,today.minute))

header ={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
url="https://news.naver.com/"
res = requests.get(url,headers=header)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

news_list = soup.find("ul",attrs = {"class":"hdline_article_list"}).find_all("li")
for index, news in enumerate(news_list):
    title = news.find("a").get_text().strip()
    link = url + news.find("a")["href"]
    print("{}. {}".format(index+1,title))
    print("  (링크: {})".format(link))
