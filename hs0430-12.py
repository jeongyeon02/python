import random
ranNum = random.randint(1, 100)                                          # 1부터 100까지의 숫자를 랜덤으로 생성
print("홀,짝을 맞히세요")                                                 # 문자형 홀,짝을 맞히세요 출력
userNum = int(input('홀수 또는 짝수를 입력하세요: '))                     # 변수 userNum을 숫자형으로 선언하여 입력  
if ranNum % 2 == userNum % 2:                                            # 변수 ranNum를 2로 나눈 나머지가 변수 userNum을 2로 나눈 나머지와 같으면  
 print("맞혔습니다")                                                     # 문자형 맞혔습니다 출력
else:                                                                    # 그게 아니면 문자형 틀렸습니다 출력 
 print("틀렸습니다") 
print("난수 : ", ranNum)                                                 # 문자형 난수:와 변수 ranNum 출력
print("사용자 : ", userNum)                                              # 문자형 사용자:와 변수 userNum 출력

입력값:
77
출력값:
맞혔습니다  
난수: 99
사용자: 77  
