MAX = 10000
compare = list(range(1, MAX))


def make_next(curr):
    return sum(list(map(int, list(str(curr))))) + curr


def recursive_seq(n, recursive_start):
    if n >= MAX:
        return
    elif n == recursive_start:
        pass
    else:
        try:
            compare.index(n)
            compare.remove(n)
        except:
            return
    recursive_seq(make_next(n), recursive_start)


for c in compare:
    recursive_seq(c, c)

for self_num in compare:
    print(self_num)
