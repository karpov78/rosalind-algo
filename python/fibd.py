cache = {}


def fib(n, m):
    if n <= 0:
        return [0] * m
    if n == 1:
        return [1] + [0] * (m - 1)
    if n == 2:
        return [0, 1] + [0] * (m - 2)
    if n in cache:
        return cache[n]
    p = fib(n - 1, m)
    res = [0] * m
    for i in range(1, m):
        res[0] += p[i]
        if i < m - 1:
            res[i + 1] = p[i]
    res[1] = p[0]
    cache[n] = res
    return res


if __name__ == '__main__':
    n, m = (int(x) for x in input().split())
    print(sum(fib(n, m)))
