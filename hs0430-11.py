# 입력한 정수들의 계산

num1 = int(input('첫 번째 정수를 입력하세요: '))  # 변수 num1을 숫자로 선언하여 입력
num2 = int(input('두 번째 정수를 입력하세요: '))  # 변수 num1을 숫자로 선언하여 입력
num3 = int(input('세 번째 정수를 입력하세요: '))  # 변수 num1을 숫자로 선언하여 입력

print("곱 : ", num1 * num2)                      # 문자형 곱: 과 변수 num1, num2의 곱을 출력
print("제곱 : ", num2 ** num3)                   # 문자형 제곱: 과 변수 num2의 num3승 출력
print("평균: ", (num1 + num2 + num3) / 3)        # 문자형 평균: 과 변수 num1, num2, num3의 합을 3으로 나눈 값을 출력 

# 사용자 정보 입력하기
print("사용자 정보를 입력하세요")                # 문자형 사용자 정보를 입력하세요 출력
name = input('이름: ')                          # 변수 name 입력
old = input('나이 : ')                          # 변수 old 입력
birth = input('생일: ')                         # 변수 birht 입력
major = input('전공 : ')                        # 변수 major 입력
print("이름)", name)                            # 문자형 이름)과 변수 name 출력
print("나이)", old)                             # 문자형 나이)와 변수 old 출력
print("생일)", birth)                           # 문자형 생일)과 변수 birth 출력
print("전공)", major)                           # 문자형 전공)과 변수 major 출력
 
입력값:
50
5
6
유정연
20
06/10
역사철학부 철학전공

출력값: 
곱 :  250
제곱 :  15625
평균:  20.333333333333332 
사용자 정보를 입력하세요
이름) 유정연
나이) 20
생일) 06/10
전공) 역사철학부 철학전공
