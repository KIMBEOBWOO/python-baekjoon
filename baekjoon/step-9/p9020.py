def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


def find_goldbach_partition(n: int):
    primes = prime_list(n)  # 짝수 n 보다 작은 소수 리스트
    p_index = int(len(primes)/2)-1  # 소수 리스트의 길이 상 중간 인덱스
    result = [0, 0]
    # print('initial p_index', p_index, primes[p_index])

    # 합이 n 을 넘는 최소 두 인접 인덱스 p_index 를 찾음
    if primes[p_index] + primes[p_index + 1] < n:
        while primes[p_index] + primes[p_index + 1] <= n and not result[0]:
            if primes[p_index] + primes[p_index + 1] == n:
                # 종료 로직
                # print('finish', primes[p_index], primes[p_index + 1])
                result = [primes[p_index], primes[p_index + 1]]
                break
            if primes[p_index]*2 == n:
                # 종료 로직
                # print('finish', primes[p_index], primes[p_index + 1])
                result = [primes[p_index], primes[p_index]]
            p_index += 1
    elif primes[p_index] + primes[p_index + 1] == n or primes[p_index]*2 == n:
        if primes[p_index] + primes[p_index + 1] == n:
            # 종료 로직
            # print('finish', primes[p_index], primes[p_index + 1])
            result = [primes[p_index], primes[p_index + 1]]
        if primes[p_index]*2 == n:
            # 종료 로직
            # print('finish', primes[p_index], primes[p_index + 1])
            result = [primes[p_index], primes[p_index]]
    else:
        while primes[p_index] + primes[p_index + 1] >= n and not result[0]:
            if primes[p_index] + primes[p_index + 1] == n:
                # 종료 로직
                # print('finish', primes[p_index], primes[p_index + 1])
                result = [primes[p_index], primes[p_index + 1]]
                break
            if primes[p_index]*2 == n:
                # 종료 로직
                # print('finish', primes[p_index], primes[p_index + 1])
                result = [primes[p_index], primes[p_index]]
            p_index -= 1

    # print(primes)
    # print(p_index, primes[p_index], primes[p_index + 1])
    # k = p_index - 1

    if result[0]:
        print(result[0], result[1])

    # 찾은 p_index 로 합이 n 인 최소 인덱스 차 소수를 찾음
    while p_index != len(primes) and not result[0]:
        k = p_index
        # print(k, p_index)
        while primes[p_index] + primes[k] >= n and k >= 0:
            # print('k ', k, p_index)
            if primes[k] + primes[p_index] == n:
                # 종료 로직
                # print('finish in last logic',
                #       primes[p_index], primes[k])
                result = [primes[k], primes[p_index]]
                # return [primes[k], primes[p_index]]
                print(primes[k], primes[p_index])
                break
            k -= 1
        p_index += 1


N = int(input())

for _ in range(N):
    n = int(input())
    find_goldbach_partition(n)
