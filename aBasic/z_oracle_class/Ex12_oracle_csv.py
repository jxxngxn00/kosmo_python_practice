#Ex12_oracle_csv.py
import cx_Oracle as oci
import csv

def createDBTable():
    conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
    sql = '''
        CREATE TABLE supply
        (
            id              number       primary key,
            Supplier_Name   varchar2(50),
            Invoice_Number  varchar2(50),
            Part_Number     varchar2(30),
            Cost            number,
            Purchase_Date   date
        )
    '''
    cursor = conn.cursor()
    cursor.execute(sql)

    sql2 = 'CREATE SEQUENCE seq_supply_id'
    cursor.execute(sql2)

    cursor.close()
    conn.close()

def saveDBTable(data):
    conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
    sql = '''
    INSERT INTO supply
        VALUES(seq_supply_id.NEXTVAL, :0, :1, :2, :3, :4)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, data)

    print('입력 완료')

    cursor.close()
    conn.commit() #중요 : commit
    conn.close()

def viewDBTable(table):
    conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
    sql = 'SELECT * FROM ' + table
    cursor = conn.cursor()
    cursor.execute(sql)

    datas = cursor.fetchall()
    for row in datas:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

    cursor.close()
    conn.close()

if __name__ == '__main__' :
    # (1) 테이블 생성
    # createDBTable()

    # (2-0) 입력확인
    # imsi = ['kosmo', '9999', '8888', 1000, '2022-12-24']
    # saveDBTable(imsi)

    # (2) CSV 파일을 읽어서 -> db 입력
    # file = open('supply.csv', 'rt', encoding='utf-8-sig')
    # datas = csv.reader(file)
    # # print(datas) # object
    #
    # header = next(datas, None)  # data의 제목행 뒤로 밀어냄
    # #print('header > ', header)  # 제목행 출력
    #
    # for row in datas:
    #     #print(row)
    #     saveDBTable(row)

    # (3) 테이블 내용 출력
    viewDBTable('supply')