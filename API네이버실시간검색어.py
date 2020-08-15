import requests
import json

headers = {
    'authority': 'apis.naver.com',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'origin': 'https://www.naver.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.naver.com/',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8',
}

params = (
    ('frm', 'main'),
    ('ag', '30s'),
    ('gr', '4'),
    ('ma', '-2'),
    ('si', '-2'),
    ('en', '-2'),
    ('sp', '-2'),
)

response = requests.get('https://apis.naver.com/mobile_main/srchrank/srchrank', headers=headers, params=params)
naver_data = json.loads(response.text)
result = []
for data in naver_data['data']:
    if data['keyword_synonyms'] is None:
        result.append([data['keyword'],None])
    else:
        result.append([data['keyword'],data['keyword_synonyms']])
print(result)

idx = 1
for keyword, synonyms in result:
    if synonyms is not None:
        print(f'{idx}번째 검색어:{keyword}, 연관검색어:{synonyms}')
    else:
        print(f'{idx}번째 검색어:{keyword}')