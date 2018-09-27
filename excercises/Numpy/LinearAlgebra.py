import numpy as np

n = int(input())

arr = np.array([input().split() for _ in range(n)], dtype=np.float32)

print(round(np.linalg.det(arr), 2))
