import util

__author__ = 'ekarpov'

data = util.readDNAs()
s1 = data[0][1]
s2 = data[1][1]

trans = 0
trav = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        if s1[i] == 'A' and s2[i] == 'G' or s1[i] == 'G' and s2[i] == 'A':
            trans += 1
        elif s1[i] == 'C' and s2[i] == 'T' or s1[i] == 'T' and s2[i] == 'C':
            trans += 1
        else:
            trav += 1

print(trans / trav)