# 입력
# 첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의
# 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다. 단, 2 ≤ N ≤ 50, 10 ≤ x,y ≤ 200 이다.

# 출력
# 여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다.
# 단, 각 덩치 등수는 공백문자로 분리되어야 한다.


# stdin 입력부
N = int(input())
person = []
for _ in range(N):
    person.append(tuple(map(int, input().split())))


# 두 사람의 덩치 비교
def compare_two_person(p1: tuple, p2: tuple) -> bool:
    return p1[0] > p2[0] and p1[1] > p2[1]


ranks = []
for i in range(N):
    ith_rank = 1
    for j in range(N):
        if i != j and compare_two_person(person[j], person[i]):
            ith_rank += 1

    ranks.append(ith_rank)


print(" ".join(map(str, ranks)))
