import re

s = input()
pattern = "(?=({0:s}))".format(input())

m = list(re.finditer(pattern, s))

#print(m)

if len(m) > 0:
    print(*[(i.start(1), i.end(1) - 1) for i in m], sep='\n')
else:
    print((-1, -1))
