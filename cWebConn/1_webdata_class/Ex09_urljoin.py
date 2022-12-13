"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""
#import urllib
from urllib import parse
baseUrl = 'http://www.example.com/html/a.html'

print(parse.urljoin(baseUrl, 'b.html'))         # /html/b.html (상대경로)
print(parse.urljoin(baseUrl, 'sub/c.html'))     # /html/sub/c.html (상대경로)
print(parse.urljoin(baseUrl, '/sub/d.html'))    # /sub/d.html (절대경로)

print(parse.urljoin(baseUrl, '../temp/e.html')) # /temp/e.html ( ../ : 부모폴더로 이동 )

print(parse.urljoin(baseUrl, 'http://www.daum.net')) # 새로운 도메인일 경우 : 경로이동X 덮어씀


