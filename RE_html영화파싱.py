import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)
movie_data_soup = BeautifulSoup(response.text,'html.parser')

movie_list = movie_data_soup.select(
    'div[id=wrap]>div[id=container]>div[id=content]>div[class=article]>div[class=obj_section]>div[class=lst_wrap]>ul[class=lst_detail_t1]>li'
)

final_movie_data=[]
for movie in movie_list:
    a_tag = movie.select_one('dl>dt>a')
    movie_title = a_tag.text
    movie_code = a_tag['href'].split('code=')[1]
    # print(movie_title)
    # print(movie_code)

    movie_data = {
        'title':movie_title,
        'code':movie_code
    }
    final_movie_data.append(movie_data)

# print(final_movie_data)

# iframe이라는 녀석때문에 src로 크롤링 하면 되지만, 추후 자바스크립트가 방해할때를 대비해서.
# curl 방법을 이용해서 크롤링을 이어나가자.

# =============================================
# curl -- >> 파이썬 언어로 바꿔주는 사이트.
# https://curl.trillworks.com/
# ==============================================


# 영화 리뷰의 경우 headers 체크를 따로 하지 않아서 굳이 보낼 필요가 없다.
# 즉 삭제 시켜도 된다는 의미!
# headers = {
#     'authority': 'movie.naver.com',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-dest': 'iframe',
#     'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
#     'accept-language': 'ko,en-US;q=0.9,en;q=0.8',
#     'cookie': 'NNB=DDX3AC4DCYCF6; NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; nx_ssl=2; ASID=79b32aaf000001733726fc7000000061; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _fbp=fb.1.1595227419852.1738571819; _ga_4BKHBFKFK0=GS1.1.1595227419.1.1.1595227465.14; _ga=GA1.1.1468214155.1595227420; _ga_7VKFYR6RV1=GS1.1.1596174655.1.1.1596174671.44; page_uid=UyqD5wp0J1ZssgSb5D8ssssssHC-202676; csrf_token=ddd6a88c-b8c6-42ec-b82f-ac5aa5ae3ec7',
# }
final_review_data =[]
for movie in final_movie_data:
    movie_code = movie['code']

    params = (
        ('code', movie_code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', params=params) #headers=headers,
    review_soup = BeautifulSoup(response.text,'html.parser')

    review_list = review_soup.select(
        'body > div > div > div.score_result > ul > li'
    )
    # print(len(review_list))
    final_review_data.append(review_list)
# print(final_review_data)
    count = 0
    for review in review_list:
        score = review.select_one('div[class=star_score] > em').text
        reple = ''

        # 리뷰가 긴 경우와 일반적인 경우 2가지가 있다. 예외 처리가 필요.
        # 일반적인 경우를 먼저 처리 하는 것이 효율적인 방법입니다!
        if review.select_one(f'div[class=score_reple] > p > span[id=_filtered_ment_{count}] > span[id=_unfold_ment{count}]') is None:
            reple = review.select_one(f'div[class=score_reple] > p > span[id=_filtered_ment_{count}]').text.strip()
        # 리뷰가 긴 경우 처리
        elif review.select_one(f'div[class=score_reple] > p > span[id=_filtered_ment_{count}] > span[id=_unfold_ment{count}]'):
            reple = review.select_one(f'div[class=score_reple] > p > span[id=_filtered_ment_{count}] > span > a')['data-src']

        count += 1
        print(score, reple)

    # 또 다시 예외 처리를 해야할 것이 눈에 보인다.



