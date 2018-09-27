import numpy as np

n, m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], dtype=np.int32)
b = np.array([input().split() for _ in range(n)], dtype=np.int32)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
