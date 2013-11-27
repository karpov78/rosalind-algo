import sys


def overlap(s, t):
    n = 0
    for k in range(1, len(s)):
        if s[-k:] == t[:k]:
            n = k
    return n


data = []
while True:
    s = input()
    if not s: break
    data.append(s)

data_size = len(data)
if data_size == 0:
    sys.exit()

str_len = len(data[0])
half_len = str_len / 2
while len(data) > 1:
    s = data[0]
    for i in range(1, len(data)):
        left = overlap(s, data[i])
        if left > half_len:
            data[0] += data[i][- str_len + left:]
            del data[i]
            break
        right = overlap(data[i], s)
        if right > half_len:
            data[0] = data[i][:str_len - right] + s
            del data[i]
            break
print(data[0])

