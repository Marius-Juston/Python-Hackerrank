import numpy as np

n, m, p = map(int, input().split())
array = []
for _ in range(n + m):
    t = np.array([input().split()], dtype=np.int32)
    array.append(t)

print(np.concatenate(array, axis=0))
