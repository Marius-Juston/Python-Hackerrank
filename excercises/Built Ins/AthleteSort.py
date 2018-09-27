n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
k = int(input())

# print(data)
# print(k)
# [print(*sorted(d, key=lambda x: x[k])) for d in data]
[print(*d) for d in sorted(data, key=lambda x: x[k])]
