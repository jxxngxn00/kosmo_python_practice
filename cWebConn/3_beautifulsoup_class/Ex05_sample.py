"""
    기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
        - 데이타 가져오기     ` requests 모듈
                             ` urllib.request 모듈의 urlopen() 이용
        - 데이타 추출    BeautifulSoup 이용
"""

from bs4 import BeautifulSoup
from urllib import request as req




# 1. 데이타 가져오기
#  http://www.kma.go.kr > [생활과산업] > [서비스] > [인터넷] > RSS
rssUrl = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
res = req.urlopen(rssUrl)
# print(res)  # [결과] http.client.HTTPResponse object

# 2. 필요 데이타 추출하기
soup = BeautifulSoup(res, 'html.parser')
# print(soup) # 파싱 결과확인
# print('-'*100)

# 도시 / 시간대별 날씨상태등 추출하여 출력
'''
# 시간대별 날씨상태
times = soup.select('location data tmEf')

for time in times:
    t = time.text.strip()   #시간대
    wDict = {}

    city = time.parent.parent.select_one('city') #도시이름
    weather = time.parent.select_one('wf') #날씨
'''

# 도시별 날씨상태
cities = soup.select('location city')

for city in cities:
    #도시 이름
    cName = city.text.strip()
    print('-'*50)
    print('도시 :', cName)

    #시간대 / 날씨
    times = city.parent.select('tmEf')
    for time in times:
        t = time.text.strip()
        w = time.parent.select_one('wf')
        w = w.text.strip()
        print(t, w)
