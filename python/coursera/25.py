profile = [{'A': 0.2, 'C': 0.1, 'G': 0, 'T': 0.7}, {'A': 0.2, 'C': 0.6, 'G': 0, 'T': 0.2},
           {'A': 0, 'C': 0, 'G': 1, 'T': 0}, {'A': 0, 'C': 0, 'G': 1, 'T': 0}, {'A': 0, 'C': 0, 'G': 0.9, 'T': 0.1},
           {'A': 0, 'C': 0, 'G': 0.9, 'T': 0.1}, {'A': 0.9, 'C': 0, 'G': 0.1, 'T': 0},
           {'A': 0.1, 'C': 0.4, 'G': 0, 'T': 0.5}, {'A': 0.1, 'C': 0.1, 'G': 0, 'T': 0.8},
           {'A': 0.1, 'C': 0.2, 'G': 0, 'T': 0.7}, {'A': 0.3, 'C': 0.4, 'G': 0, 'T': 0.3},
           {'A': 0, 'C': 0.6, 'G': 0, 'T': 0.4}]

s = raw_input()

res = 1
for i in range(len(s)):
    res *= profile[i][s[i]]
print res