#함수 부분
def varchange(list):
    for k in list:
        k=int(input("변수 "+k+"의 값을 입력하세요. : "))
def conchange(list):
    for k in list:
        k=int(input("상수 "+k+"의 값을 입력하세요. : "))
#1. 변수와 상수 입력하기
var=list(input("변수를 입력하세요. : "))
con=list(input("상수를 입력하세요. : "))
#2. 식 입력하기
f=input("식을 입력하세요. : ")
revise(f)
varchange(var)
conchange(con)
#3. 프로그램의 활용 설정(근삿값 찾기, 그래프 그리기 등)
#4. 수치 해석 프로그램 작동
#5. 결과 출력
