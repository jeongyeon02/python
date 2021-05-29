# 배송료 계산 알고리즘

price= int(input("상품의 가격을 입력하세요: "))  # 변수 price를 숫자형으로 선언하여 입력
if price > 50000:                               # 가격이 50000보다 크면 배송료는 0
 shipping_cost = 0 
else:                                           # 가격이 50000보다 작거나 같으면 배송료 3000 
 shipping_cost = 3000
print(shipping_cost)                            # 배송료 출력  

# 성적입력받아서 합격 유무 출력

grade = int(input("성적을 입력하세요: "))       # 변수 grade를 숫자형으로 선언하여 입력
if grade >= 80 :                                # 점수가 80보다 같거나 크면 문자형 합격입니다 출력
 print("합격입니다")
else :                                          # 점수가 80보다 작으면 문자형 불합격입니다 출력
 print("불합격입니다")

입력값:
54300
92
출력값:
0
합격입니다
  
  
  
