from urllib import request as req
from bs4 import BeautifulSoup
from urllib import parse
import os


# [1] 녹색 글자만 추출하여 출력
html = req.urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

soup = BeautifulSoup(html,'html.parser')

green = soup.select('#text span.green')
for t in green:
    print(t.text)

# [2] 아이템과 가격을 추출
html2 = req.urlopen('http://www.pythonscraping.com/pages/page3.html')
soup2 = BeautifulSoup(html2, 'html.parser')

trs = soup2.select('table#giftList tr.gift')
for tr in trs:
    td = tr.select('td')
    name = td[0].text.strip().replace('/', '_')
    price = td[2].text.strip().replace('/', '_')

    print('이름 >>', name)
    print('가격 >>', price)



# [3] 책 제목과 저자만 추출, 이미지 다운
html3 = req.urlopen('https://wikidocs.net/')
soup3 = BeautifulSoup(html3, 'html.parser')

items = soup3.select('#books .media')

os.makedirs('prac_imgs', exist_ok=True) # 이미지 저장 폴더 생성

for item in items:
    
    # 책 이름, 저자 추출
    name = item.select_one('.media-body h4.media-heading').text.strip().replace('/', '_')
    author = item.select_one('.media-body .book-detail a.menu_link').text.strip().replace('/', '_')

    print('이름 >>', name)
    print('저자 >>', author)

    # 이미지 저장

    img = item.select_one('.media-left .book-image-box img') #이미지 태그 추출
    url = 'https://wikidocs.net'

    i = parse.quote_plus(parse.urljoin(url, img.attrs['src']), safe="://") #url 한글깨짐 문제 해결 : quote_plus 사용
    print('이미지 저장', i)
    req.urlretrieve(i, 'prac_imgs/'+name+'.jpg')  # 이미지 저장