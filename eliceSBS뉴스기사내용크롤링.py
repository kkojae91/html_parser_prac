import requests
from bs4 import BeautifulSoup

URL = 'https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

news_data = soup.select('#container > div > div.w_news_list.type_issue > ul > li')
# print(news_data)
# print(len(news_data))
url_list = []
for news in news_data:
    # url 추출
    a_tag = news.select_one('a')
    url_list.append('https://news.sbs.co.kr' + a_tag['href'])
print(url_list)

# 각 url마다 기사 내용 출력
result_text_list = []
for url in url_list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_list = soup.select_one('#container > div.w_inner > div.w_article > div.w_article_cont > div > div.article_cont_area > div.main_text > div')
    result_text_list.append(text_list.text.replace('\n',''))
print(result_text_list)
