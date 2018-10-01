def median(nums):
    if len(nums) % 2 == 0:
        return int(sum(nums[len(nums) // 2 - 1:len(nums) // 2 + 1]) / 2)
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


N = int(input())
nums = sorted([int(num) for num in input().split()])
Q1, Q2, Q3 = quartiles(N, nums)
print(Q1)
print(Q2)
print(Q3)
