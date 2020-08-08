# import requests
# from bs4 import BeautifulSoup

# 동아뉴스 href, title 추출하기.
first_URL = 'https://sports.donga.com/ent?p='
last_URL = '&c=02'

result_news_list = []
for i in range(1,82,20):
    base_URL = str(i)
    URL = first_URL + base_URL + last_URL
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    news_list = soup.select('#contents > div.sub_content > div.list_content > ul > li')
    # print(len(news_list))

    for news in news_list:
        a_tag = news.select_one('div > span.tit > a')
        result_news_list.append([a_tag.text, a_tag['href']])

print(result_news_list)

##################
# 네이트 뉴스 href, title 추출하기.
import requests
from bs4 import BeautifulSoup

URL = 'https://news.nate.com/recent?mid=n0100&type=c&date=20200809&page='
nate_result = []
for i in range(1,6):
    response = requests.get(URL+str(i))
    # print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.select('#newsContents > div.postListType.noListTitle > div.postSubjectContent > div.mduSubjectList')
    # print(len(news_list))
    for news in news_list:
        news_tag = news.select_one('div > a > span.tb > strong.tit')
        # nate_result.append(news_tag.text)
        news_href = news.select_one('div > a')
        nate_result.append(['https'+news_href['href'],news_tag.text])

print(nate_result)