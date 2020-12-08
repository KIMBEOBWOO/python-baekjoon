# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 소수란? 자연수 중 합성수가 아닌 수


N = int(input())
numbers = list(map(int, input().split()))


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


count_of_primes = 0
for n in numbers:
    if is_prime_number(n):
        count_of_primes += 1

print(count_of_primes)
