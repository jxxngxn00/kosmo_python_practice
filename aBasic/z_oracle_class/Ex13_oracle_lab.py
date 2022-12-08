"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
import cx_Oracle as oci

class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소:", self.addr)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    name = input('이름은? ')
    phone = input('전화번호는? ')
    email = input('이메일은? ')
    addr = input('주소는? ')

    # c = Contact(name,phone,email,addr)
    # data = [c.name, c.phone_name, c.email, c.addr]

    data = [name, phone, email, addr]

    # Contact 객체를 생성하고 DB 에 입력 -> 그냥 배열로 생성하고 DB에 입력하는 걸로 변경
    conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
    sql = '''
        INSERT INTO cont
            VALUES(:0, :1, :2, :3)
        '''
    cursor = conn.cursor()
    cursor.execute(sql, data)

    print('>> 입력 완료')

    cursor.close()
    conn.commit()
    conn.close()

def print_contact():
    # (2)
    #  테이블의 전체 레코드 출력
    conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
    sql = 'SELECT * FROM cont'
    cursor = conn.cursor()
    cursor.execute(sql)

    datas = cursor.fetchall()
    for row in datas:
        c = Contact(row[0], row[1], row[2], row[3]) # Contact 객체 생성 후 한줄씩 결과값 출력
        c.print_info()

    cursor.close()
    conn.close()

def delete_contact(name):
    # (3)
    # 해당이름과 같은 요소를 찾아서 삭제
    conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
    sql = "DELETE FROM cont WHERE name LIKE '" + name +"'"

    cursor = conn.cursor()
    cursor.execute(sql)
    print('>> ',name,'삭제됨')

    cursor.close()
    conn.commit()
    conn.close()

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)

def createTbl():
    conn = oci.connect('scott/tiger@192.168.0.35:1521/xe')
    sql = '''
            CREATE TABLE cont
            (
                name    varchar2(50),
                phone   varchar2(50),
                email   varchar2(50),
                addr     varchar2(50)
            )
        '''
    cursor = conn.cursor()
    cursor.execute(sql)

    cursor.close()
    conn.commit()
    conn.close()
    print('테이블 생성')

if __name__ == "__main__":
    # createTbl()
    run()
