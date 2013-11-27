MODULO = 1000000
__author__ = 'ekarpov'

(n, k) = (int(x) for x in input().split(' '))

p = 1
for i in range(k):
    p *= n - i
    if p > MODULO:
        p %= MODULO
print(p)