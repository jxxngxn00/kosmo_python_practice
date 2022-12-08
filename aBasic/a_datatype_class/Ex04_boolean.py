# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False
print(not hungry)           # 결과값 : False

print(hungry and sleepy)    # 결과값 : False
print(hungry or sleepy)     # 결과값 : True


"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"           True
                    ""              False
        리스트       [1,2,3]         True       
                    []              False
        튜플         ()              False
        딕셔너리     {}               False
        숫자형       0이아닌 숫자      True
                    0                False
                    None             False

"""
if '아':
    print('True')
else:
    print('False')

if []:
    print('True2')
else:
    print('False2')

if 0:
    print('True3')
else:
    print('False3')

if -1:
    print('True3')
else:
    print('False3')

msg = '행복합시다'
# '행'의 index : 0 -> False
if msg.find('행') :
    print('ok')
else :
    print('no')

# '가'의 index : -1 (존재하지 않음) -> True
if msg.find('가') :
    print('ok')
else :
    print('no')

# 문자열 포함여부 확인하기 : 비교연산자 사용
if msg.find('행') == -1 :
    print('찾는 문자열이 없습니다')
else :
     print('문자열이 있습니다 : ',msg.find('행'))

# 문자열 포함여부 확인하기 : in 연산자 사용
if '행' in msg :
    print('찾는 문자열이 있습니다')
else : print('찾는 문자열이 없습니다')