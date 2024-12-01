with open('./1/input.txt', 'r') as f:
    input = [a.strip().split('   ') for a in f]

setA = sorted([int(a[0]) for a in input])
setB = sorted([int(a[1]) for a in input])
diffs = [abs(setA[i] - setB[i]) for i in range(0,len(setA))]
print(f'Part A: sum of deviations = {sum(diffs)}') #test assert = 11

sim = [a*setB.count(a) for a in setA]
print(f'Part B: sum of calibration = {sum(sim)}') #test assert = 31