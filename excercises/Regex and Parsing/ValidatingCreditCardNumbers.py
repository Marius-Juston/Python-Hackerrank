import re

patten = r'(?!.*(\d)(-?\1){3}.*)^[456]\d{3}-?(?:\d{4}-?){3}$'

n = int(input())

for _ in range(n):
    if bool(re.match(patten, input())):
        print("Valid")
    else:
        print("Invalid")
