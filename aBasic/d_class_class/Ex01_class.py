"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

''' 자바인 경우
class Sample {
    String data = "Hello";
    String name;
    Sample(String name) {
        this.name = name;
    }
}
Sample s = new Sample("홍길동");

'''
class Sample :
    data = "Hello"
    def __init__(self, name, age):  # 생성자 함수
        self.name = name
        self.age = age
        print('__init__ 호출')

    def __del__(self):              # 메모리 해제
        print('__del__ 호출')
s=Sample('홍길동', 55)
print(s.data)
print(s.name)
print(s.age)
del s
print('-'*20)


"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근

    [자바인 경우]
    class Sample{
        int a;
        static int b;
    }
    Sample s1 = new Sample();
    Sample s2 = new Sample();
    Sample s3 = new Sample();
    
"""

class Book:
    cnt = 0
    def __init__(self, title):
        self.title = title
        self.cnt += 1

    def output(self):   # self : this 역할
        pass

    @classmethod
    def output2(cls):
        cls.cnt += 1

b1 = Book('행복이란')
b1.output2()
b2 = Book('먹고살자')
b2.output2()
print(b1.cnt)
print(b2.cnt)
print(Book.cnt)

print('-'*20)





'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''

class Animal:
    def move(self):
        print('동물은 움직인다')

class Human(Animal): #상속
    #overriding
    def move(self):
        print('인간은 두 발로 걷는다')

class Wolf(Animal):
    #overriding
    def move(self):
        print('늑대는 네 발로 달린다')

class Werewolf1(Wolf, Human):
    
    # 오버라이딩 가능
    def move(self):
        print('늑대인간은 두 발로 달린다')

class Werewolf2(Human, Wolf):
    pass


h=Human()
h.move()

w = Wolf()
w.move()

ww1 = Werewolf1()
ww1.move()       # Wolf.move 호출 : Wolf를 먼저 썼기 때문에

ww2 = Werewolf2()
ww2.move()       # Human.move 호출 : Human을 먼저 썼기 때문에
print('-'*20)

