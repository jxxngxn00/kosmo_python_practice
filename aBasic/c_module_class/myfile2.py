# import mypackage.mymodule                                    # 같은 폴더에 없는 모듈 불러오기
# print('오늘의 날씨 : ', mypackage.mymodule .get_weather())
# print('오늘은 ', mypackage.mymodule .get_date(), '요일입니다')

from mypackage import mymodule as mm
print('오늘의 날씨 : ', mm.get_weather())
print('오늘은 ', mm.get_date(), '요일입니다')
