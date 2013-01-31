MODULO = 1000000
__author__ = 'ekarpov'

n = int(input())

sum = 1
for i in range(n):
    sum *= 2
    if sum > MODULO:
        sum %= MODULO
print(sum)