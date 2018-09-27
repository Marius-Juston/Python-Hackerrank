import numpy

r, c = map(int, input().split())

l = []
for _ in range(r):
    l.append(list(map(int, input().split())))

l = numpy.array(l)
print(l.transpose())
print(l.flatten())
