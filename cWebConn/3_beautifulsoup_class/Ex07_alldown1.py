"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse
from urllib import request


def enum_links(html, base):
    # -------------------------------------
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a')
    result = []

    for a in links:
        href = a.attrs['href']
        # print(href)
        url = parse.urljoin(base, href)
        # print(url)
        result.append(url)

    return result


'''
    함수명     : enum_links
    인자      : html, base
    리턴값     : result[]
    역할      : 해당 페이지의 a 태그를 찾아서 링크 생성 후 배열로 반환
'''

if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)  # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)
