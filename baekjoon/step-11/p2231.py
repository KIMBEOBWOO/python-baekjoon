# 문제
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.
# 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다

N = int(input())


def num_to_digits(n: int) -> list:
    # 정수를 입력받아 자리수 단위로 쪼개 리스트로 만드는 함수
    return list(map(int, list(str(n))))


def digits_to_num(arr: list) -> list:
    origin_num = 0
    for i in range(len(arr)):
        origin_num += arr[i]*10**i
    return origin_num


MAX = len(num_to_digits(N))

origin = [0 for i in range(MAX-1)]
origin = [1] + origin


# print(origin)
cnt = digits_to_num(origin)
# end = digits_to_num(num_to_digits(N))
# print(MAX, origin, cnt, N)

while cnt < N:
    # print(cnt)
    if sum(num_to_digits(cnt)) + cnt == N:
        # print('-'*20)
        # print(sum(num_to_digits(cnt)) + cnt, cnt)
        print(cnt)
        break
    cnt += 1

if cnt == N:
    print(0)

# def sum_of_each_digits(arr: list) -> int:
#     # 자리수 리스트를 입력받아 분해합을 구하는 함수
#     sum_of_digits = sum(arr)
#     for i in range(len(arr)):
#         print('')


# end_arr = [9 for i in range(MAX)]


# print(sum(num_to_digits(198)) + 198)
# total_cnt = 0
# digit_cnt = 0
# print(num)
