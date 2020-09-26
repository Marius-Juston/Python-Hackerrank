from typing import List


def level_is_smaller(cubes):
    if len(cubes) <= 1:
        return True

    if cubes[0] >= cubes[-1]:
        val = cubes.pop(0)
    else:
        val = cubes.pop(-1)

    if val < max(cubes[0], cubes[- 1]):
        return False

    return level_is_smaller(cubes)


def is_possible(cubes: List[int]) -> bool:
    if len(cubes) <= 2:
        return True

    return level_is_smaller(cubes)


def is_possible_non_req(cubes):
    if len(cubes) <= 2:
        return True

    while len(cubes) > 1:
        if cubes[0] >= cubes[-1]:
            val = cubes.pop(0)
        else:
            val = cubes.pop(-1)

        if val < max(cubes[0], cubes[- 1]):
            return False

    return True


if __name__ == '__main__':
    with_file = True

    if with_file:
        with open("input04.txt") as file:
            N = int(file.readline())

            for _ in range(N):
                file.readline()
                cubes = list(map(int, file.readline().split()))

                # print()
                print("Yes" if is_possible_non_req(cubes) else "No")
    else:
        N = int(input())

        for _ in range(N):
            input()
            cubes = list(map(int, input().split()))

            # print()
            # print("Yes" if is_possible(cubes) else "No")
            print("Yes" if is_possible_non_req(cubes) else "No")
