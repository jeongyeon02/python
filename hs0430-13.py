# 일교차에 따른 메시지 설정하기
morningTemp = int(input('아침 최저 기온을 입력하세요: '))  # 변수 morningTemp를 숫자형으로 선언하여 입력
afternoonTemp = int(input('오후 최고 기온 : '))            # 변수 afternoonTemp를 숫자형으로 선언하여 입력
gapTemp = afternoonTemp - morningTemp                      # 변수 gapTemp를 변수 afternoonTemp과 morningTemp의 차로 선언
if gapTemp >= 10:
  print("감기 조심해라")                                   # 만약 변수 gapTemp가 10보다 크거나 같으면 감기 조심해라 출력
elif afternoonTemp >= 30: 
  print("더우니까 집에 있어")                              # 변수 afternonnTemp가 30보다 크거다 같으면 문자형 더우니까 집에 있어 출력

# 메시지 길이에 따른 분류 
userMessage = input('메시지를 입력하세요: ')                # 변수 userMessage를 숫자형으로 선언하여 입력
MsgLen = len(userMessage)                                  # 변수 MsLen를 함수 len으로 정의
if MsgLen <= 50:                                           # 변수 MsLendl 50보다 작거나 같으면 
 print("SMS로 발송됩니다")                                  # 문자형 SMS로 발송됩니다 출력
else:                                                   
 print("MMS로 발송됩니다")                                  # 그렇지 않으면 문자형 MMS로 발송됩니다 줄력  
print("메시지 길이 : ", MsgLen)                             # 문자형 메시지 길이와 변수 MsLen 출력

입력값:
18
27
시험 공부 하기 싫다
출력값:
SMS로 발송됩니다
메시지 길이: 11
