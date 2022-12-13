# 내장 모듈 이용

from urllib import request

url = 'http://www.google.com'
site = request.urlopen(url)

page = site.read()
print(page)
print('-'*50)
print(site.status)

headers = site.getheaders()
print(headers)              # 리스트 안에 튜플로 나옴


for header in headers:
    print(header[0],'>>',header[1])