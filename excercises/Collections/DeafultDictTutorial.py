from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    d[input()].append(i + 1)

for i in range(m):
    var = d[input()]

    if len(var) == 0:
        print("-1")
    else:
        print(*var)
