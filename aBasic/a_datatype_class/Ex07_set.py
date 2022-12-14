# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }

s = set()               # 빈 집합을 생성
s = set([1, 2, 3, 1, 1])
# print(s)
s = {1, 2, 3, 1, 1}
# print(s)

# 인덱스로 출력 불가능 : print(s[0]) 이런거 안됨
s1 = {1,2,3,1,1}        # s1 = {1,2,3}
s2 = {3,4,5,6,3,4}      # s2 = {3,4,5,6}

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s2 -s1)