from collections import namedtuple

n = int(input())
Student = namedtuple("Student", input())

average = 0
for i in range(n):
    average += int(Student(*input().split()).MARKS)

print(average / n)
