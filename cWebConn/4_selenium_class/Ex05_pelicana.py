from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

# [연습]
print('-' * 20)
print('매장명 - 전화번호')
print('-' * 20)

# 페이지 수 만큼 돌림
for page_no in range(1, 11):
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d' % page_no)
    html = driver.page_source
    # print(html)
    time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select('table tbody tr')

    # 매장명 - 전화번호
    for data in datas:
        dLi = data.select('td.t_center')
        # print(dLi)
        
        # 더이상 읽어올 td가 없을 경우 반복문 종료
        if len(dLi) == 0:
            break

        name = dLi[0].text.strip()
        num = dLi[1]
        number = []
        # print(num)

        # 번호가 여러개일 경우
        if '<br/>' in str(num):
            # print(num)
            
            # 줄바꿈 기준으로 쪼갬
            number = str(num).split('<br/>')

            for i in range(len(number)):
                number[i] = number[i].strip() #공백 제거

            number[0] = number[0][-12:] # 태그 제거 -- 이게 최선인지는..모르겟음
            number[1] = number[1][:11]

        # 그 외 : 번호가 하나일 경우
        else :
            number = num.text.strip()

        print(name, '-', number)
