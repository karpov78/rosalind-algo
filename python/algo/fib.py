fib_cache = {}


def fib(f_index):
    if f_index == 1 or f_index == 2:
        return 1
    if f_index in fib_cache:
        return fib_cache[f_index]
    f = fib(f_index - 1) + fib(f_index - 2)
    fib_cache[f_index] = f
    return f


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
