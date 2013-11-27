__author__ = 'ekarpov'

s = input()
t = input()

res = []
i = 0
for c in t:
    while s[i] != c:
        i += 1
    res.append(i + 1)
    i += 1

print(' '.join([str(x) for x in res]))

