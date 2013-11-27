s = raw_input()
k = int(raw_input())

kmers = {}
longest = []
longest_count = 0

for i in range(0, len(s) - k + 1):
    kmer = s[i:i + k]
    if kmer in kmers:
        kmers[kmer] += 1
    else:
        kmers[kmer] = 0

    if kmers[kmer] > longest_count:
        longest_count = kmers[kmer]
        longest = [kmer]
    elif kmers[kmer] == longest_count:
        longest.append(kmer)

print ' '.join(longest)