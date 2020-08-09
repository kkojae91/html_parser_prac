import requests
from bs4 import BeautifulSoup

URL = 'https://news.naver.com/main/list.nhn?sid1=10'

section = input('정치,경제,사회,문화,세계,과학 중 하나를 입력하세요.')
sections ={
    '정치' : '0',
    '경제' : '1',
    '사회' : '2',
    '문화' : '3',
    '세계' : '4',
    '과학' : '5'
}
response = requests.get(URL+sections[section])
soup = BeautifulSoup(response.text,'html.parser')
# print(soup)

news_href = soup.select('#main_content > div.list_body.newsflash_body > ul.type06_headline > li')
# print(len(news_href))
# 각섹션별 url 추출
url_list = []
for news in news_href:
    a_tag = news.select_one('dl > dt:nth-child(2) > a')
    url_list.append(a_tag['href'])
# print(url_list)

result_text = []
for url in url_list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    section_text = soup.select_one('#articleBodyContents')
    result_text.append(section_text.text.replace('\t','').strip())

print(result_text)
