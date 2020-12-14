import pandas as pd
import numpy as np
import math

x = np.arange(3)
print(x)
y = pd.Series(x)


def func_S_k(n: int):
    return int(math.floor(-1 + math.sqrt(1+8*n))/2)


for i in range(1, 10):
    print(i, func_S_k(i))

# # 초기값

# def remake_possible(index: int, possible: list):
#     # possible 재설정
#     return [possible[index]-1, possible[index], possible[index]+1]


# def calculate_count(x, y):
#     p = x+1
#     count = 1
#     possible = [0, 1, 2]
#     mid = math.floor((y-x)/2)
#     print(mid)

#     if y-1 - x <= max(possible):
#         p = y-1
#     else:
#         while p < mid:
#             print('p : ', p, possible)
#             if mid - p <= max(possible):

#                 count += 1
#                 possible = remake_possible(possible.index(mid-p), possible)
#                 p = mid
#             else:
#                 count += 1
#                 p += max(possible)
#                 possible = remake_possible(2, possible)

#         while p < y-1:
#             # print('p : ', p)
#             if y - 1 - p <= max(possible):
#                 count += 1
#                 p = y-1
#             else:
#                 count += 1
#                 p += max(possible)
#                 possible = remake_possible(2, possible)
#         count += 1

#     print(count)

# for t in range(T):
#     x, y = list(map(int, input().split()))
#     calculate_count(x, y)
