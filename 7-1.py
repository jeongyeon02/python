def sayHello(name, age):                # 정의된 함수 sayHello에 이름과 나이를 인자로 받음
    if age < 21:                        # 나이가 21살보다 적으면 문자형 고마워 출력 
        print( name + "고마워")          
    elif age <=40 and age >= 21:        # 나이가 40살보다 적고 10살보다 21살보다 같거나 많으면 문자형 고맙습니다 출력
        print( name + "고맙습니다")    
    else:                               # 나이가 40살보다 같거나 많으면 문자형 감사합니다 출력
        print( name + "감사합니다")  
        
sayHello("은형", 20)
sayHello("승현", 22)
sayHello("가형", 39)
sayHello("명수", 61)

출력값:
은형고마워
승현고맙습니다
가형고맙습니다
명수감사합니다  
