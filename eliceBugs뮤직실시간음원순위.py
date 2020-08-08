import requests
from bs4 import BeautifulSoup

URL = 'https://music.bugs.co.kr/chart'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
music_list = soup.select('#CHARTrealtime > table > tbody > tr')
# print(music_list)
# print(len(music_list))
music_chart = []
for music in music_list:
    a_tag = music.select_one('th > p > a')
    music_chart.append(a_tag.text)
print(music_chart)