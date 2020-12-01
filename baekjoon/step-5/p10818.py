# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 1. python min , max
N = int(input())
numbers = list(map(int, input().split()))

# minNumber = min(numbers)
# maxNumber = max(numbers)

# print(minNumber, maxNumber)

minNumber, maxNumber = numbers[0], numbers[0]
# 2. 브포
for n in numbers:
    if minNumber > n:
        minNumber = n
    if maxNumber < n:
        maxNumber = n

print(minNumber, maxNumber)
