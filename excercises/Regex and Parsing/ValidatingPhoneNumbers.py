import re

n = int(input())

for _ in range(n):
    print("YES" if bool(re.match(r"[789]\d{9}", input())) else "NO")
