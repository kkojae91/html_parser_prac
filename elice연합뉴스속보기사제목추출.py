import requests
from bs4 import BeautifulSoup

URL = 'https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0011801564'
response = requests.get(URL)
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
news_header = soup.select('#main_content > div.list_body.newsflash_body')
# print(news_header)
# print(len(news_header))
result = []
for news in news_header:
    tag1 = news.select_one('div>dl>dt>a[class="nclicks(cnt_flashart)"]')
    result.append(tag1.text)
    # tag2 = news.select('div>dl>dd>ul>li>a')
    # for i in tag2:
    #     result.append(i.text)
    tag3 = news.select('ul>li>a')
    for j in tag3:
        result.append(j.text)
    


print(result)