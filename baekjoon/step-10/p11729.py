
# 하노이탑 이동 횟수 함수

def hanoi(n: int, current, target):
    if n == 1:
        return 1
    else:
        hanoi(n-1, current, 5-(target+current))
        print(current, target)
        hanoi(n-1, 5-(target+current), target)


# 하노이 탑 이동 경로 함수


def hanoi_move(n: int):
    # 어차피 Pn = 2*Pn-1 + 1 임
    print('')


print(hanoi(3, 1, 3))
