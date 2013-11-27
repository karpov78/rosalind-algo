from python.util import getHammingDistance, readDNAs
from python.matrix import Matrix

__author__ = 'ekarpov'


def p_distance(s, t):
    return getHammingDistance(s, t) / len(s)


data = readDNAs()
matrix = Matrix(len(data), default=float(0), format="%.5f")

for i in range(len(data)):
    for j in range(len(data)):
        distance = p_distance(data[i][1], data[j][1])
        matrix[i, j] = distance

print(matrix)