# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

N = int(input())


def is_hansu(n: int) -> bool:
    # n 은 3자리수
    digits = list(map(int, list(str(n))))
    return digits[2]-digits[1] == digits[1]-digits[0]


def num_of_hansu(n: int):
    if n < 100:
        return n
    else:
        count = 99
        for i in range(100, n+1):
            if is_hansu(i):
                count += 1
        return count


print(num_of_hansu(N))
