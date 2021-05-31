# 짝수 홀수 판별하기
# 1)
sm_int = int(input('정수를 입력하세요: '))       # 변수 sm_int를 숫자형으로 선언하여 입력
if (sm_int % 2) != 0 :                           # 만약 변수 sm_int를 2로 나눈 나머지가 0이 아니라면
 print("홀수입니다")                             # 문자형 홀수입니다 출력
else:                                            # 그게 아니면 문자형 짝수입니다 출력
 print("짝수입니다") 

# 2)
def printEvenOdd():                              # 함수를 printEvenOdd로 정의
 if userData % 2 == 0:                           # 만약 userDate를 2로 나누었을 때 나머지가 0이면
   print("짝수 입니다")            # 문자형 입력한 정수는 짝수입니다 출력
 else:                                           # 그게 아니면 문자형 입력한 정수는 홀수 입니다 출력
   print("홀수 입니다")
userData = int(input('정수를 입력하세요. '))     # 변수 userData를 숫자형으로 선언하여 입력
printEvenOdd()                                  

입력값:
5
2
출력값:
홀수입니다
짝수입니다
