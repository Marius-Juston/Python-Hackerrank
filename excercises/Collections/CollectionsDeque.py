from collections import deque

n = int(input())

queue = deque()
for i in range(n):
    line = input().split()
    getattr(queue, line[0])(*line[1:])

print(*queue)
