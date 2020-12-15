
# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는다.

# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

N, M = list(map(int, input().split()))
origin = list(map(int, input().split()))

origin.sort()

S = 0
finish_flag = True

i = len(origin) - 1
while 2 <= i and finish_flag:
    j = i-1

    while 1 <= j and finish_flag:
        k = j - 1

        while 0 <= k and finish_flag:
            temp = origin[k] + origin[j] + origin[i]
            if temp == M:
                print(temp)
                finish_flag = False
                break
            if S < temp < M:
                S = temp
                break
            if temp < M:
                break
            k -= 1
        j -= 1
    i -= 1

if finish_flag:
    print(S)
