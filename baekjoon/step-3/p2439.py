N = int(input())

for n in range(1, N+1):
    whiteSpace = (N - n)*' '
    repeat = '*' * n
    print(whiteSpace+repeat)


