import math

# 테스트 케이스 횟수 입력
T = int(input())


def func_S_k(n: int):
    k = int(math.floor(-1 + math.sqrt(1+8*n))/2)
    check = int((k+1)*(k)/2)

    if check == n:
        return [k, check]
    else:
        return [k, int((k+1)*(k+2)/2)]


def cal_min_count(p, mid, count):
    d = mid - p

    if d <= 2:
        return d
    else:
        move, limit = func_S_k(d)
        gap = limit - d

        # print(move, limit, gap)
        if gap == 0:
            count += move
        else:
            count += (move + 1)
        return count


for t in range(T):
    x, y = list(map(int, input().split()))

    mid = x+math.floor((y-x)/2)
    # print('mid : ', mid)
    p = x+1
    count = 1

    if y - x <= 2:
        print(y-x)
    elif p + 2 < y-1:
        count_up = cal_min_count(p, mid, 1)
        p = mid
        mid = y - 1

        # print('step 2  ', p, mid)
        count_down = cal_min_count(p, mid, 1)

        # print('up : ', count_up, count_down)
        print(count_up + count_down)
    else:
        print(3)
