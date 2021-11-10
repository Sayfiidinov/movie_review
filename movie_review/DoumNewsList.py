# Doum News 목록을 for 문을 돌면서 제목과 본문을 수집

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

url_list = doc.select('ul.list_news2 a.link_txt')

for i, href in enumerate (url_list):
    # 기사 1건의 제목과 본문을 수집하는 코드
    new_url = href['href']
    result = requests.get(new_url)

    # 2.BeautifulSoup 라이브러르 사요해서 원하는 정보만 주출
    doc = BeautifulSoup(result.text, 'html.parser')

    # h3 tag 중에서   class가  tit_view인  tag를 가져오세요

    title = doc.select('h3.tit_view')[0].get_text()  # . => class
    contents = doc.select('section p')
    contents.pop(-1)
    content = ''
    for info in contents:
        content += info.get_text()
    # 자손 산택자

    print('### NEWS -> {} ###################################################################'.format(+i))
    print('# URL: {}'.format(new_url))
    print('# content: {}'.format(title))
    print('# content: {}'.format(content))
