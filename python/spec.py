from python.util import getSymbol

__author__ = 'ekarpov'

specter = []
while True:
    s = input()
    if not s: break
    specter.append(float(s))

specter = specter[::-1]
protein = ''

prev_w = specter[0]
for w in specter[1:]:
    weight = prev_w - w
    prev_w = w
    protein = getSymbol(weight) + protein

print(protein)