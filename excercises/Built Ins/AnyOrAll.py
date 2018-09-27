_, data = input(), input().split()
positive = [int(v) > 0 for v in data]
palindrome = [v == v[::-1] for v in data]
print(all(positive) and any(palindrome))
