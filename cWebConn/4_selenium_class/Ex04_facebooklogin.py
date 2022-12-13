from selenium import webdriver

usr='ji4ever'
psd=''

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)   # 3초 대기

# driver.get('http://www.facebook.com')
# driver.get('http://www.daum.net')
# driver.get('http://www.naver.com')
# driver.get('http://www.instagram.com')


email = driver.find_element_by_id('email')
passwd = driver.find_element_by_id('pass')

email.send_keys(usr)
passwd.send_keys(psd)

btn = driver.find_element_by_name('login')
btn.click()
driver.implicitly_wait(2)