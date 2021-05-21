# 리스트 = list() = []

x = ["해리포터", "하울의 움직이는 성", "위플래쉬", "베일리 어게인"]   # 변수 x를 영화 리스트로 선언
print(x)                                                             # 영화 리스트 출력

x = ["해리포터", "하울의 움직이는 성", "위플래쉬", "베일리 어게인"]   # 순서대로 0, 1, 2, 3
print(x[0])                                                          # 0번째 자리에 있는 해리포터 출력(리스트 안의 특정값을 선정하여 출력 가능)

x[2] = "소울"                                                        # x 리스트 2번째를 문자형 소울로 선언 
print(x)                                                             # x 리스트의 2번째 위플래시가 소울로 변화되어 출력

x = ["해리포터", "하울의 움직이는 성", "위플래쉬", "베일리 어게인"]   # 변수 x를 영화 리스트로 선언
y = ["팝콘", "버터 오징어", "나초", "콜라"]                          # 변수 y를 영화관 음식 리스트로 선언
z= [1,2,3,4]
print(x+y)                                                          # 리스트끼리 합하여 출력 가능
print(y+z)                                                          # 리스트 안의 개념이 문자형이든 숫자형이든 구분하지 않고 합하여 출력 가능
print(x[5])                                                          # 리스트 범위 안에 있지 않으면 출력 불가능

출력값:
['해리포터', '하울의 움직이는 성', '위플래쉬', '베일리 어게인']
해리포터
['해리포터', '하울의 움직이는 성', '소울', '베일리 어게인']
['해리포터', '하울의 움직이는 성', '위플래쉬', '베일리 어게인', '팝콘', '버터 오징어', '나초', '콜라']
['팝콘', '버터 오징어', '나초', '콜라', 1, 2, 3, 4]