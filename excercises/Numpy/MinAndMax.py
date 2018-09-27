import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for i in range(n)], dtype=np.int32)
print(arr.min(axis=1).max())
