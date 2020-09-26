def wrapper(f):
    def fun(l: str):
        l = ['+91' + r if len(r) == 10 else r.replace('0', '+91', 1) if r.startswith('0') else '+' + r if r.startswith(
            '91') else r for r
             in l]
        l = [r[:3] + ' ' + r[3:8] + ' ' + r[8:] for r in l]

        f(l)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
