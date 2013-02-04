from python import util

MODULO = 1000000

rna = input()

result = 1
for s in rna:
    codes = util.reverseRNA[s]
    result *= len(codes)
    result %= MODULO

print(result * (len(util.reverseRNA[''])) % MODULO)