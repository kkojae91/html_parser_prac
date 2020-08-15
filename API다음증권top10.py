import requests
import json

headers = {
    'authority': 'finance.daum.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://finance.daum.net/',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8',
    'cookie': '_TI_NID=iok9mjEFfnWoNqMjDA5hhaGdhtcUGpCqrcdJLPWDjNtcUs2XzU7yJ4JKnARDKlnIb3mDgmrHIz3Ewu42FY2QPQ==; webid=c05cd2e0c0af11eabb11000af759d260; webid_ts=1594167166734; _ga=GA1.2.1939417052.1597468543; _gid=GA1.2.1325581147.1597468543; __T_=1; TIARA=C5fCCSQ.auDaLYG87_Wdjyc8sJv.FOWniDKOeuJMiyw4ZvIu16c_-U.DVHHvm5o4hfucIJq5ztF_5vtvnu4maA00; webid_sync=1597471114719; _dfs=bEJRM3lBNkVMaGdyMm5BWDRyTzJlY0diOEZuOVNtZjJLd3RWOVNPUTdIV1FqZkZvN2ppQ0ZSNldaU1lXVll6RzkveWVYMytIL1lIcXdlQ01BR20ycnc9PS0tNk9iVGc0M0R4WG5ZWnZacWoxTXF4Zz09--061f2b74e8d2b774ad60e8d77b2b3c39e9282707',
}

params = (
    ('limit', '10'),
)

response = requests.get('https://finance.daum.net/api/search/ranks', headers=headers, params=params)
daum_data = json.loads(response.text)
result = []
for data in daum_data['data']:
    result.append([data['rank'],data['name'],data['tradePrice']])

print(result)