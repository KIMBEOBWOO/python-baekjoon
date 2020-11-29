pre = int(input())
curr = list(map(int, list(input())))
result = 0

curr.reverse()

for i in range(len(curr)):
    eachResult = pre*curr[i]
    print(eachResult)
    result += eachResult * 10 ** (i)

print(result)
