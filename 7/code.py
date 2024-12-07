with open('./7/input.txt', 'r') as f:
    input = [a.strip().split(':') for a in f]

correctA = []; correctB = []
for eq in input:
    vals = list(map(int, eq[1].split()))
    res = int(eq[0])

    ansA = [vals[0]]; ansB = [vals[0]]
    for v in vals[1:] :
        ansA = [a * v for a in ansA] + [a + v for a in ansA]
        ansB = ([a * v for a in ansB] + [a + v for a in ansB] +
            [int(str(a) + str(v)) for a in ansB])

    if res in ansA : correctA.append(res)
    if res in ansB : correctB.append(res)

print(f'Part A: answer = { sum(correctA) }') #test assert = 3749
print(f'Part B: answer = { sum(correctB) }') #test assert = 