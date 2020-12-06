# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

# 출력
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

import math

N = int(input()) - 1


def func_2d_metric(c: int):
    result = (
        (-3 + math.sqrt(9+12*c))/6,
        (-3 - math.sqrt(9+12*c))/6,
    )
    if result[0] >= 0:
        return result[0]
    else:
        return result[1]


print(int(math.ceil(func_2d_metric(N)))+1)
