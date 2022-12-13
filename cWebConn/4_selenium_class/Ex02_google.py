'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''
from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)   # 3초 대기

driver.get('http://www.daum.net')
# driver.get('http://www.google.com')
# driver.get('http://www.naver.com')

#----------------------------------------------
# [2]
# 다음, 구글
search_bt = driver.find_element_by_name('q')

# 네이버의 경우
# search_bt = driver.find_element_by_name('query')

search_bt.send_keys('집 가고싶다')
search_bt.submit()