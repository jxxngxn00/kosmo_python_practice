# [ 파이썬 + 디비 절차 ]

import cx_Oracle as oci

# 1. 연결객체 얻어오기 ( Connection )
conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
print(conn.version)
# 2. sql 문장
sql = 'select * from emp'

# 3. cursor 객체 얻어오기
cursor = conn.cursor()

# 4. 실행
cursor.execute(sql)

datas = cursor.fetchall()
#print(datas)
for row in datas:
    print(row[0], row[1], row[2])

# 5. cursor 객체 닫기
cursor.close()

# 6. 연결객체 닫기
conn.close()
