import requests
from bs4 import BeautifulSoup


def crawling(soup) :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    result = []
#     div = soup.find('div', class_='list_issue')
#     # print(div)
#     for a in div.find_all('a'):
#         # print(a.text)
#         result.append(a.get_text())

    news_header = soup.select('#yna_rolling')
    # print(news_header)
    for news in news_header:
        # a_tag = news.select_one('div>div>div>a')
        print(news)
        news = news.text.split('\n')
        result.append(news)
    return result
    
def main() :
    url = "http://www.naver.com"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    print(crawling(soup))


if __name__ == "__main__" :
    main()
