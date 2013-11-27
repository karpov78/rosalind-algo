__author__ = 'ekarpov'

MODULO = 1000000

df = lambda x: (df(x - 2) * x) % MODULO if x > 2 else 1

if __name__ == '__main__':
    n = int(input())
    print(df(2 * n - 5))
