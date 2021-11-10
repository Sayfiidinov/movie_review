## Daum News에서 페이지를 돌면서 뉴스 기사의 제목과 본문을 수집


import requests
from bs4 import BeautifulSoup

# Page 반복
i = 0
for page_number in range(1, 4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(page_number)
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')

    url_list = doc.select('ul.list_news2 a.link_txt')

    # 뉴스 목록 반복(in Page)
    for url in url_list:
        i += 1  # News Count
        print('■■ NEWS → {}번 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(i))
        new_url = url['href']
        print('# URL: {}'.format(new_url))
        result = requests.get(new_url)
        doc = BeautifulSoup(result.text, 'html.parser')
        title = doc.select('h3.tit_view')[0].get_text()
        contents = doc.select('section p')
        contents.pop(-1)  # 기자 정보 삭제
        content = ''  # 본문 총합
        for info in contents:
            content += info.get_text()

        print('# 뉴스 제목: {}'.format(title))
        print('# 뉴스 본문: {}'.format(content))