import numpy as np

np.set_printoptions(sign=' ')
arr = np.array(input().split(), dtype=np.float32)

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
