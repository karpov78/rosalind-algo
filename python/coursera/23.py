import math

matrix = []
while True:
    s = raw_input()
    if not s:
        break
    matrix.append(s.split(' '))

entropy = 0
for j in range(len(matrix[0])):
    m = {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}
    for i in range(len(matrix)):
        m[matrix[i][j]] += 1
    e = 0
    for v in m.values():
        p = v / len(matrix)
        e += 0 if p == 0 else p * math.log(p, 2)
    entropy += -e

print entropy