
# 링의 위치를 암시적으로 표현하는 3 colums list
ring = [1, 2, 3]
N = int(input())


def hanoi_cal(n: int):
    # 하노이탑 이동 횟수 함수
    if n == 1:
        return 1
    else:
        return hanoi_cal(n-1)*2 + 1


def hanoi_move(n: int, prv: int, nxt: int):
    # 하노이탑 이동 경로 함수
    if n == 1:
        print(ring[prv], ring[nxt])
        return 1
    else:
        hanoi_move(n-1, prv, 3-(prv+nxt))
        print(ring[prv], ring[nxt])
        hanoi_move(n-1,  3-(prv+nxt), nxt)


print(hanoi_cal(N))  # 횟수 먼저 계산 (문제 요구 사항)
hanoi_move(N, 0, 2)  # 이동 경로 계산
