# 코딩을 배울 수 있는 나이 출력

you_name = str(input("이름을 입력하세요: "))                        # 변수 you_name을 문자형으로 선언하여 입력
you_age = int(input("나이를 입력하세요: "))                         # 변수 you_age를 숫자형으로 선언하여 입력                   
if you_age <= 25 :                                                  # 나이가 25보다 작거나 같으면
 print(you_name + "님께서는, 코딩을 배우실 수 있는 연령이십니다.")   # 변수 you_name과 문자형 님께서는, 코딩을 배우실 수 있는 연령이십니다.를 합산하여 출력
else:
 print(you_name + "님, 배움에 나이는 상관이 없습니다.")              # 나이가 25보다 크다면 변수 you_name과 문자형 님, 배움에 나이는 상관이 없습니다.를 합산하여 출력

입력값:
유정연
20
출력값:
유정연님께서는, 코딩을 배우실 수 있는 연령이십니다. 
