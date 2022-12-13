"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

'''
    함수명     : download_file
    인자      : url
    리턴값     : savepath (저장할 폴더 경로)
    역할      : 해당 url의 index.html 페이지를 폴더에 저장함 
               (폴더가 없을경우 새로 생성)
'''

def download_file(url):
    p = parse.urlparse(url)
    # print('1 -', p)
    savepath = './' + p.netloc + p.path
    # print ('2 -', savepath)

    # 링크 생성
    if re.search('/$', savepath):  # 정규화
        savepath += 'index.html'
        # print('3 -', savepath)

    # 같은 이름의 디렉토리가 없을 경우 하위 폴더 생성
    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir, exist_ok=True)  # makedir : 하위폴더 생성 불가능 /

    try:
        request.urlretrieve(url, savepath)  # index.html 다운로드
        time.sleep(2)
        print('download -', url)
        return savepath

    except:
        print('fail download :', url)
        return None


if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)
