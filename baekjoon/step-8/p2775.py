# 입력
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)

# 출력
# 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

apart = [list(range(0, 15))]

for i in range(1, 15):
    apart.append([0 for i in range(0, 15)])
    for j in range(1, 15):
        apart[i][j] = apart[i-1][j] + apart[i][j-1]

T = int(input())

for t in range(T):
    room = [0, 0]
    for i in range(2):
        room[i] = int(input())
    print(apart[room[0]][room[1]])
