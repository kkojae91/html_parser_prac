import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

movie_selection = soup.select(
    'div[id=wrap]>div[id=container]>div[id=content]>div[class=article]>div[class=obj_section]>div[class=lst_wrap]>ul[class=lst_detail_t1]>li'
)

for movie in movie_selection:
    a_tag = movie.select_one('dl>dt>a')
    movie_title = a_tag.text
    movie_code = a_tag['href'].split('code=')[1]
    # print(movie_title)
    # print(movie_code)

    movie_data = {
        'movie_title':movie_title,
        'movie_code':movie_code
    }
    print(movie_data)