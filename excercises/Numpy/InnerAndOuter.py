import numpy as np

a = np.array(input().split(), dtype=np.int32)
b = np.array(input().split(), dtype=np.int32)

print(np.inner(a, b))
print(np.outer(a, b))
