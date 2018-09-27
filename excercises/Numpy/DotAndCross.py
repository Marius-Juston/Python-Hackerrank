import numpy as np

n = int(input())

A = np.array([input().split() for _ in range(n)], dtype=np.int32)
B = np.array([input().split() for _ in range(n)], dtype=np.int32)

print(np.dot(A, B))
