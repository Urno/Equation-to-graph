#함수 부분
def varchange(list):
    for k in list:
        k=int(input("변수 "+k+"의 값을 입력하세요. : "))
def conchange(list):
    for k in list:
        k=int(input("상수 "+k+"의 값을 입력하세요. : "))
def revise(x):
    print("함수의 각 기능 부분을 분류")
#1. 변수와 상수 입력하기
var=list(input("변수를 입력하세요. : "))
con=list(input("상수를 입력하세요. : "))

#2. 식 입력하기
f=input("식을 입력하세요. : ")
revise(f)
varchange(var)
conchange(con)

#3. 프로그램의 활용 설정
def value(x):
    print("미지수의 값을 변화시키는 함수")
def constant(x):
    print("상수의 값을 변화시키는 함수")

#4. 수치 해석 프로그램 작동
print("Numpy")

#5. 결과 출력
def graph(x):
    print("그래프 출력 함수")
