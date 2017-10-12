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
varchange(var)
conchange(con)
