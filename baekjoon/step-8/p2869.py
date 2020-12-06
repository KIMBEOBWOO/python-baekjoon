# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

import math
A, B, V = list(map(int, input().split()))
# day = 0
# while (A-B)*day < (V-A):
#     day += 1

print(int(math.ceil((V-A)/(A-B))+1))
