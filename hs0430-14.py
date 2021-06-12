import random 

ranNum = random.randint(1, 3)                                              # 1부터 3까지의 숫자를 랜덤으로 생서
print("가위, 바위, 보 중 선택하세요")                                       # 문자형 가위, 바위, 보 중 선택하세요 출력

userNum = int(input('1 == 가위, 2 == 바위, 3 == 보: '))                     # 변수 userNum을 숫자형으로 선언하여 입력
if (ranNum == 1 and userNum == 2) or (ranNum == 2 and userNum == 3)         # 만약 난수가 1 입력한 숫자가 2, 난수가 2 입력한 숫자가 3, 난수가 3 입력한 숫자가 1이면
or (ranNum == 3 and userNum == 1):                                          # 문자형 Win! 출력
  print(" Win!")
elif (ranNum == 1 and userNum == 3) or (ranNum == 2 and userNum == 1)       # 그렇지 않고 난수가 1 입력한 숫자가 3, 난수가 2 입력한 숫자가 1, 난수가 3 입력한 숫자가 2이면  
or (ranNum == 3 and userNum == 2):                                          # 문자형 Lose! 출력
  print("Lose!")                                                             
elif ranNum == userNum:                                                     # 그렇지 않고 난수와 입력한 숫ㅈ자가 같으면  
  print("Draw!")                                                            # 문자형 Draw! 출력

print("컴퓨터: ", ranNum)                                                   # 문자형 컴퓨터:와 변수 ranNum 출력
print("사용자: ", userNum)                                                  # 문자형 사용자:와 변수 userNum 출력

입력값:
3
출력값:
가위, 바위, 보 중 선택하세요
Win!
컴퓨터: 2
사용자: 3  
