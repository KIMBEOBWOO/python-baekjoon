
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.


while True:
    try:
        A,B = list(map(int,input().split()))
        print(str(A+B))
    except:
        break 
   

# 중요! 런타임 에러
# 왜? input 을 위와 같이 map, list , int 를 사용할 경우 다른 문자나 
# 터미널 명령어가 들어올 경우 에러 발생, 반드시 핸들링 할 것
    




