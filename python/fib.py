def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + k * fib(n - 2)

if __name__ == '__main__':
    n, k = (int(x) for x in input().split())
    print(fib(n))
