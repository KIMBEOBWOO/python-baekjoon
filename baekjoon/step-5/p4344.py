# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# import math
C = int(input())

root = []
for c in range(C):
    case = list(map(int, input().split()))
    root.append(case)

for eachCase in root:
    sum_of_case = 0
    for j in range(1, len(eachCase)):
        sum_of_case += eachCase[j]

    count_of_upper = 0
    avg_of_case = (sum_of_case/eachCase[0])

    for k in range(1, len(eachCase)):
        if eachCase[k] > avg_of_case:
            count_of_upper += 1

    print('%0.3f' % float(count_of_upper/eachCase[0]*100)+'%')
