# 변수를 선언할 때 의미를 두고 정한다
pay_rate = 8750                                                   # 시급을 8750으로 선언 
hours_worked = int(input("일을 한 전체 시간을 입력하세요: "))      # 숫자형으로 선언된 일한 시간을 입력
monthly_pay = pay_rate * hours_worked                             # 월급을 시급과 일한 시간의 곱으로 선언

print(monthly_pay)                                                # 월급을 출력
