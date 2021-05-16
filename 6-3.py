#함수 3

# 다른 이름들을 사용하고 자 할 때

# 4)
a = "은형"
b = "채현"
c = "수진"
d = "수아"
a1 = 5
a2 = 2

# def chat(name1, name2):                       #함수들이 인자라는 것을 받는다.(파라미터, 아규먼트로 명칭)
#     print("%s: 우리 몇 시에 만나?" % name1)
#     print("%s: 2시에 만나자" % name2)

# chat(a, b)
# chat(c, d)


# 5)
def chat(name1, name2, time):           #함수들이 인자라는 것을 받는다.(파라미터, 아규먼트로 명칭)
    print("%s: 우리 몇 시에 만나?" % name1)
    print("%s: %d시에 만나자" % (name2, time))

chat("a", "b", a1)
chat("c", "d", a2)

출력값:
은형: 우리 몇 시에 만나?
채현 5시에 만나자
수진: 우리 몇 시에 만나?
수아: 2시에 
