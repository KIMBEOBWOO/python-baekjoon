import math


def cal_K_by_Sk(Sk: int):
    k = int(math.floor(-1 + math.sqrt(1+8*Sk))/2)
    gap = int(k*(k+1)/2) != Sk  # gap 이 존재하지 않으면 0, 존재하면 1
    gap_size = Sk - int(k*(k+1)/2)

    return [k, gap, gap_size]


# 테스트 케이스 횟수 입력
T = int(input())

# result = []
for t in range(T):
    x, y = list(map(int, input().split()))  # 시작점 , 끝점
    mid = x+math.floor((y-x-1)/2) if y-x % 2 == 1 else x + \
        math.floor((y-x)/2)  # 중간 지점 (짝일 경우 x에 붙임)

    count = 0
    up_result = cal_K_by_Sk(mid-x)
    down_result = cal_K_by_Sk(y-mid)

    count += up_result[0]
    count += down_result[0]

    # if up_result[1] or down_result[1]:
    #     count += 1

    if up_result[2] + down_result[2] > max([up_result[0]+1, down_result[0]+1]):
        count += 2
    elif 0 < up_result[2] + down_result[2] <= max([up_result[0]+1, down_result[0]+1]):
        count += 1

    print(count)
    # result.append(count)

# print('\n======================\n ', result)
# 7
# 3
# 92681
# 92681
# 92681
# 92681
# 92680
# 3
# 3
# 2
# 1
# 1
# 2
# 3
# 3
