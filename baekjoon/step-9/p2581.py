# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

import math

M = int(input())
N = int(input())


def is_prime_number(k: int) -> bool:
    if k <= 3:
        if k == 2 or k == 3:
            return True
        else:
            return False
    elif k % 2 == 0:
        return False
    else:
        for i in range(3, int((k-1)/2)+1, 2):
            if k % i == 0:
                return False

        return True


min_prime_number = math.inf
sum_of_primes = 0

for n in range(M, N + 1):
    if is_prime_number(n):
        if min_prime_number == math.inf:
            min_prime_number = n
        sum_of_primes += n

print(sum_of_primes)
print(min_prime_number)
