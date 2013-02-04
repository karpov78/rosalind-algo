factors = [2, 2, 2, 1.5, 1, 0]

str_pop = input()
pop = []
for s in str_pop.strip().split():
    pop.append(int(s))

result = 0
for i in range(len(pop)):
    result += pop[i] * factors[i]
print(result)
