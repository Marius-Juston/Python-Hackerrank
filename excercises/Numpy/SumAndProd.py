import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for i in range(n)], dtype=np.int32)
print(arr.sum(axis=0).prod())
