MODULO = 1000000
__author__ = 'ekarpov'

cnk_values = {}

def c_mod(n, k):
    if k == 0 or n < k:
        return 0
    if k == 1 or k == n:
        return 1
    if (n, k) in cnk_values:
        return cnk_values[n, k]
    result = (c_mod(n - 1, k - 1) + c_mod(n - 1, k)) % MODULO
    cnk_values[n, k] = result
    return result

(n, m) = [int(x) for x in input().split(' ')]

# bug!
n += 1
m += 1

for i in range(n):
    for j in range(i):
        c_mod(i, j)

sum = 0
for i in range(m, n + 1):
    sum += c_mod(n, i)

print(sum % MODULO)
