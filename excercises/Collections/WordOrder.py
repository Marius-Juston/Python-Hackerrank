from collections import OrderedDict

n = int(input())

dicte = OrderedDict()

for i in range(n):
    line = input()
    dicte[line] = dicte.get(line, 0) + 1

print(len(dicte))
print(*dicte.values())
