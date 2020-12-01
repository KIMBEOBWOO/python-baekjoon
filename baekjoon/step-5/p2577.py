# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 같거나 크고, 1,000보다 작은 자연수이다.
# 첫째 줄에는 A×B×C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A×B×C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

import sys

multi = 1
for i in range(3):
    multi *= int(sys.stdin.readline())

eachDigit = list(map(int, list(str(multi))))
digitCount = [0 for i in range(10)]

for i in range(len(eachDigit)):
    digitCount[eachDigit[i]] += 1

for eachCount in digitCount:
    print(eachCount)
