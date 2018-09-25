n = int(input())

mathematics = []
physics = []
chemistry = []

for _ in range(n):
    s = map(int, input().split("\t"))
    m, p, c = s

    mathematics.append(m)
    physics.append(p)
    chemistry.append(c)


def find_join_mul_sum(x, y):
    sum_total = 0
    for x, y in zip(x, y):
        sum_total += x * y
    return sum_total


def sqare_sum(x):
    sum_s = 0
    for e in x:
        sum_s += (e ** 2)
    return sum_s


import math


def calculate_coefficient_of_correlation(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    sum_total = find_join_mul_sum(x, y)
    square_sum_x = sqare_sum(x)
    square_sum_y = sqare_sum(y)
    length = len(x)
    nominator = ((length * sum_total) - (sum_x * sum_y))
    denominator = math.sqrt((length * square_sum_x) - sum_x ** 2) * math.sqrt((length * square_sum_y) - sum_y ** 2)

    return round(nominator / denominator, 2)


print(calculate_coefficient_of_correlation(mathematics, physics))
print(calculate_coefficient_of_correlation(physics, chemistry))
print(calculate_coefficient_of_correlation(chemistry, mathematics))
