x = [5,2,4,6]             # 변수 x의 리스트 설정
 
for n in x:               # 리스트 x의 엘레먼트를 n에 차례로 넣음
  print(n)                # n 출력
  
y = ["야식", "후회 중"]   # 변수 y의 리스트 설정

for n in y:               # 리스트 y의 엘레먼트를 n에 차례로 넣음
  print(n)                # n 출력
  
# 엘레먼트 위치
x = [5,2,4,6]             # 변수 x의 리스트 설정
y = ["야식", "후회 중"]   # 변수 y의 리스트 설정

print(x.index(5))         # x 리스트에서 5는 0번째에 있음
print(y.index("후회 중")) # y 리스트에서 "후회 중"은 1번째에 있음 

x = [5,2,4,6]             # 변수 x의 리스트 설정
print(4 in x)             # x 리스트에 4가 있으며 True 없으면 False
print(7 in x)             # x 리스트에 7가 있으며 True 없으면 False

if 4 in x:                # x 리스트에 4가 있으면 문자형 4있음 출력
  print("4 있음")
else :                    # 그게 아니면 문자형 4 없음 출력
  print("4 없음")
  
if 7 in x:                # x 리스트에 7이 있으면 문자형 7있음 출력
  print("7 있음")      
else:                     # 그게 아니면 문자형 7 없음 출력
  print("7 없음") 
  
출력값:
5
2
4
6
야식
후회 중
0
1
True
False
4 있음
7 없음
