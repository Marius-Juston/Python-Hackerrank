import re

g = re.search(r'([a-zA-Z0-9])\1+', input())
# print(g)
# g = g


print(g.group(1) if g else -1)
