# 문제
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
# 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

# 입력
# 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3^k이며, 이때 1 ≤ k < 8이다.

# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.
import math
N = int(input())
# N = 3**6

origin = [[1 for col in range(N)] for row in range(N)]


def print_starts(array):
    for r in range(len(array)):
        each_line = ''
        for c in range(len(array[r])):
            if array[r][c] == 1:
                each_line += '*'
            else:
                each_line += ' '
        print(each_line)


def recursive_starts(r: int, c: int, size: int):
    if size == 1:
        return
    else:
        for row in range(0, int(size/3)):
            for col in range(0, int(size/3)):
                origin[r+row][c+col] = 0

        for i in range(3):
            for j in range(3):
                if not(i == 1 and j == 1):
                    recursive_starts(r-int(size/3)+int(size/3/3)+i*int(size/3),
                                     c-int(size/3) + int(size/3/3)+j*int(size/3), int(size/3))


recursive_starts(int(N/3), int(N/3), N)
print_starts(origin)


# def recursive_starts(n: int, array: list):
#     size = int(math.log10(n)/math.log10(3))

#     # print(n, size)

#     if size == 0:
#         print(array)
#         # print('-'*10)
#         print_starts(array)

#     else:
#         for r in range(3**(size-1), 3**(size-1)*2):
#             for c in range(3**(size-1), 3**(size-1)*2):
#                 # if r ==
#                 print(r, c)
#                 array[r][c] = 0

#         recursive_starts(int(n/3), array)


# # print(math.log10(N)/math.log10(3))

# recursive_starts(N, origin)
