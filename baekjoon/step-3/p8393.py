#  첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

n = int(input())
sum = 0

for i in range(n+1):
    sum += i

print(sum)
