import re

n = int(input())

pattern = r'^[-+]?\d*\.\d+$'
for i in range(n):
    print(re.match(pattern, input()))
