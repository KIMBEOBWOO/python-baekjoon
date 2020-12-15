# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.


# 시작 컬러에 대한 오더 함수의 인덱스와 주어진 한 라인에 대해 카운팅한다.
def counting_one_line(start: int, line: list) -> int:
    count = 0
    curr = start
    for i in range(M):
        if order[curr] != line[i]:
            count += 1
        curr = (curr+1) % 2
    return count


def counting_chess_squre(start: int, chess: list, col_size: tuple) -> int:
    count = 0
    curr = start

    for each_line in chess:
        count += counting_one_line(curr, each_line[col_size[0]:col_size[1]+1])
        curr = (curr+1) % 2
    return count


def counting_0_or_1_start(chess: list) -> int:
    count1 = counting_chess_squre(0, chess)
    count2 = counting_chess_squre(1, chess)

    if count1 > count2:
        return count2
    else:
        return count1


N, M = list(map(int, input().split()))
chess = []
order = ['B', 'W']

for _ in range(N):
    chess.append(str(input()))


# origin chess 판을 8x8 로 쪼개는게 필요함
for
