__author__ = 'ekarpov'
n = int(input())
A = {int(x) for x in input()[1:-1].split(', ')}
B = {int(x) for x in input()[1:-1].split(', ')}

U = set(range(1, n + 1, 1))

print(A.union(B))
print(A.intersection(B))
print(A - B)
print(B - A)
print(U - A)
print(U - B)