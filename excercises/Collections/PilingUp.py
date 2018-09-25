n = int(input())


def is_possible(cubes):
    minimum = None
    for i in range(len(cubes) // 2):
        left = cubes[i]
        right = cubes[-(i + 1)]
        mini = min(left, right)
        maxi = max(left, right)

        if minimum is None:
            minimum = mini
        elif maxi > minimum:
            return False
        else:
            minimum = mini

    return True if len(cubes) % 2 == 0 else cubes[len(cubes) // 2] <= minimum


for i in range(n):
    n = input()
    blocks = list(map(int, input().split()))

    print("Yes" if is_possible(blocks) else "No")
