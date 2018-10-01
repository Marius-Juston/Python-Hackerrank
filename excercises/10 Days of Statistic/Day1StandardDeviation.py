_, data = input(), list(map(int, input().split()))


def std(nums):
    mean = sum(nums) / len(nums)

    sum_squared = sum((x - mean) ** 2 for x in nums)

    return (sum_squared / len(nums)) ** .5


print(round(std(data), 1))
