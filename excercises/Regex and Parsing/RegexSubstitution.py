import re

n = int(input())

for _ in range(n):
    t = input()

    print(re.sub(r"(?<= )(\|\||&&)(?= )", lambda x: "and" if x.group(0) == "&&" else "or", t))
