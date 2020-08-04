import requests, csv
from bs4 import BeautifulSoup
import re

URL = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

movie_section = soup.select(
    "div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li"
)
# print(movie_section)

for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')
    movie_title = a_tag.text
    movie_code = re.findall('\d+', a_tag['href'])[0]

    # print(movie_title)
    # print(movie_code)
    movie_data = {
        'movie_title' : movie_title,
        'movie_code' : movie_code
    }
    print(movie_data)
# re.findall('\d+')