import numpy as np

np.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

arr = np.array([input().split() for i in range(n)], dtype=np.int32)
print(arr.mean(axis=1))
print(arr.var(axis=0))
print(arr.std())
