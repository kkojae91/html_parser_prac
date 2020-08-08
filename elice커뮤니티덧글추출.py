import requests
from bs4 import BeautifulSoup

URL = 'https://pann.nate.com/talk/350939697'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

reple_data = soup.select('#commentDiv > div.cmt_list > dl > dd[class="usertxt"]')
# print(reple_data)
# print(len(reple_data))
reple_list = []
# 베스트리플
best_reple = soup.select_one('#beple_content_area_541455986')
reple_list.append(best_reple.text.strip())
# best_reple = soup.select_one('#beple_content_area_541455986 > span')
# print(best_reple.text)

# 일반리플
for reple in reple_data:
    reple_tag = reple.select_one('span')
    reple_list.append(reple_tag.text.strip().replace('\n',''))

print(reple_list)