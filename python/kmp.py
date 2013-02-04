import sys

__author__ = 'ekarpov'

s = input()

p = [0] * len(s)
k = 0
for i in range(1, len(s)):
    while k > 0 and s[i] != s[k]:
        k = p[k - 1]
    if s[i] == s[k]:
        k += 1
    p[i] = k

print(' '.join([str(x) for x in p]))

#validate
for i in range(len(p)):
    if p[i] == 0:
        continue
    if s[0:p[i]] != s[i - p[i] + 1: i + 1]:
        sys.exit(1)
