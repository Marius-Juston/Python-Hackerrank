N = int(input())

values = map(int, input().split())
frequency = map(int, input().split())

nums = []

for v, f in zip(values, frequency):
    nums.extend([v] * f)

nums = sorted(nums)


def median(nums):
    if len(nums) % 2 == 0:
        return sum(nums[len(nums) // 2 - 1:len(nums) // 2 + 1]) / 2
    else:
        return nums[len(nums) // 2]


def quartiles(n, nums):
    q1 = median(nums[:len(nums) // 2])
    q2 = median(nums)
    if n % 2 == 0:
        q3 = median(nums[len(nums) // 2:])
    else:
        q3 = median(nums[len(nums) // 2 + 1:])
    return q1, q2, q3


Q1, Q2, Q3 = quartiles(N, nums)
print(round(Q3 - Q1, 1))
