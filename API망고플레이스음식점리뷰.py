import requests
import json
from bs4 import BeautifulSoup

headers = {
    'authority': 'stage.mangoplate.com',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.mangoplate.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.mangoplate.com/restaurants/B8CzA6i9Bb8Z?_branch_match_id=809268153786159236',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8',
    'if-none-match': 'W/"c9e5826d27a16c343a35c10e933acbaf"',
}

# 검색한 음식종류의 href, 음식점이름 불러오는 코드


def get_restaurant(name):
    name_URL = 'https://www.mangoplate.com/search/'+name
    response = requests.get(name_URL, headers=headers)
    # print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    restaurant_li = soup.select('body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li > div.list-restaurant-item')
    # print(len(restaurant_li))

    name_result = []
    for restaurant in restaurant_li:
        a_tag = restaurant.select_one('figure > figcaption > div > a')
        rest_name = a_tag.text.replace('\n', '').replace('\t','').replace('  ','')
        name_result.append([rest_name, a_tag['href']])

    return name_result
# print(name_result)

# 모든 리뷰를 불러오는 코드
# href = '/restaurants/B8CzA6i9Bb8Z'
def get_review(href):
    URL = f'https://stage.mangoplate.com/api/v5{href}/reviews.json?language=kor&device_uuid=6XDl115974754126911314CXsAf&device_type=web&start_index=0&request_count=50&sort_by=2'
    response = requests.get(URL, headers=headers)
    print(response)

    texts = json.loads(response.text)
    # print(len(texts))

    result =[]
    for text in texts:
        comment = text['comment']['comment']
        result.append(comment.replace('\n',''))

    return result

def main():
    name = input()
    restaurant_list = get_restaurant(name)
    print(restaurant_list)
    for restaurant in restaurant_list:
        print(restaurant[0])
        top5_review = get_review(restaurant[1])
        print(top5_review)
        break
main()

