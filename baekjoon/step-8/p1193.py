# 입력
# 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

# 출력
# 첫째 줄에 분수를 출력한다.

import math

N = int(input())


def func_2d_metric(c: int):
    return int(math.ceil((-1 + math.sqrt(1+8*c))/2))


# for i in range(0, 20):
#     print(str(i)+' : '+str(func_2d_metric(i)))

L = func_2d_metric(N)
L_start = int(L*(L-1)/2) + 1
L_end = int(L*(L+1)/2)

index = 0
if L % 2 == 1:
    # 홀수라인
    index = L_end - N
else:
    # 짝수 라인
    index = N - L_start

print(str(index+1)+'/'+str(L-index))
