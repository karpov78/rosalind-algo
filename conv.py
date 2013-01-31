__author__ = 'ekarpov'

s1 = [float(x) for x in input().split(' ')]
s2 = [float(x) for x in input().split(' ')]

spectral_conv = {}
for i1 in s1:
    for i2 in s2:
        d = round(i1 - i2, 6)
        if d in spectral_conv:
            spectral_conv[d] += 1
        else:
            spectral_conv[d] = 1

max = 0
max_key = None
for (k,v) in spectral_conv.items():
    if v > max:
        max = v
        max_key = k
print(max)
print(max_key)