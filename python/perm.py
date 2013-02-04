from python.util import printList


def perm(h, t):
    if len(t) == 0:
        print(printList(h))
        return 1
    result = 0
    for i in range(0, len(t)):
        a = t[i]
        new_tail = list(t)
        del new_tail[i]
        result += perm(h + [-1 * a], new_tail) + perm(h + [a], new_tail)
    return result

n = int(input())
f = lambda n: n - 1 + abs(n - 1) and f(n - 2) * int(n) or 1
estimate = f(2 * n)
print(estimate)
perm([], range(1, n + 1))

