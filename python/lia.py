import math

__author__ = 'ekarpov'

factorials = {}

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n in factorials:
        return factorials[n]
    else:
        result = n * factorial(n - 1)
        factorials[n] = result
        return result


def c(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

(k, N) = (int(x) for x in input().split(' '))
x = (1 << k)

sum = 0
for i in range(N, x + 1):
    sum += c(x, i) * math.pow(0.25, i) * math.pow(0.75, x - i)

print(sum)


