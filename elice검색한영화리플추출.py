import requests
from bs4 import BeautifulSoup

movie_name = input('리뷰를 보고싶은 영화를 입력하세요.')

URL = f'https://movie.naver.com/movie/search/result.nhn?query={movie_name}&section=all&ie=utf8'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
movie_href = 'https://movie.naver.com' + soup.select_one('#old_content > ul.search_list_1 > li > dl > dt > a')['href'].replace('basic','review')
# print(movie_href)
movie_code = movie_href.split('code=')[1]
# print(movie_code)

# 수업시간때 cURL 배웠던거 연습!
params = (
    ('code', movie_code),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
)

code_response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', params=params)
# print(response)
code_soup = BeautifulSoup(code_response.text, 'html.parser')
reple_list = code_soup.select('body > div > div > div.score_result > ul > li')

# result_reple_list = []
count = 0
for reple in reple_list:
    reult_reple = ''
    # 평점
    score = reple.select_one('div > em').text
    # 리플
    # span_tag = reple.select_one('div > p > span')
    # 리플이 긴 경우는 예외가 있다. 예외 처리를 해줘야 합니다.
    if reple.select_one(f'#_unfold_ment{count} > a') is None:
        result_reple = reple.select_one(f'#_filtered_ment_{count}').text.strip()
    elif reple.select_one(f'#_unfold_ment{count} > a'):
        result_reple = reple.select_one(f'#_unfold_ment{count} > a')['data-src']
    
    count += 1
    print(score,result_reple)