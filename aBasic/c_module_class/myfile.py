'''
import mymodule     # 다른 파일 끌어오기
print('오늘의 날씨 : ', mymodule.get_weather())
print('오늘은 ', mymodule.get_date(), '요일입니다')

import mymodule as mm   #별칭이 있을 경우에는 별칭만 인식함
print('오늘의 날씨 : ', mm.get_weather())
print('오늘은 ', mm.get_date(), '요일입니다')
'''

from mypackage.mymodule import get_weather, get_date   # 해당 함수만 끌어오기 (부분적 import)
print('오늘의 날씨 : ', get_weather())                   # 모듈이름 없이 끌어오는 것만 가져옴
print('오늘은 ', get_date(), '요일입니다')

