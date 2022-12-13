'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
#  html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")

html = urlopen("http://www.yes24.com/Product/Search?domain=ALL&query=python")

soup = BeautifulSoup(html, 'html.parser')

# 추출
'''
# [1]
infos = soup.select('#yesSchList div.item_info a.gd_name')
for info in infos:
    print(info.text) # 책 제목 추출

print(len(infos),'권이 검색되었습니다.')
'''

# [2]
imgs = soup.select('#yesSchList div.itemUnit img')
for img in imgs:
    name = img.attrs['alt'].strip().replace('/', '_')
    url = img.attrs['data-original']
    print(name, ':', url)

    request.urlretrieve(url, 'imgs/'+name+'.jpg')

print(len(imgs),'권이 검색되었습니다')