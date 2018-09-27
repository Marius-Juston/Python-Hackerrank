from collections import Counter

_, data = input(), Counter(map(int, input().split()))

n = int(input())

s = 0
for _ in range(n):
    value, price = map(int, input().split())

    if data[value]:  # 0 will return False otherwise True
        data[value] -= 1
        s += price

print(s)
