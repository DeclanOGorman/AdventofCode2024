with open('./2/input.txt', 'r') as f:
    input = [a.strip().split(' ') for a in f]

def isSafe(seq):
    diff = [int(seq[i]) - int(seq[i+1]) for i in range(0,len(seq)-1)]
    if sum([1 for a in diff if not(1 <= abs(a) <= 3)]) > 0 : return 0
    if sum([1 for a in diff if a < 0]) > 0 and sum([1 for a in diff if a > 0]) > 0 : return 0
    return 1

print(f'Part A: answer = {sum([isSafe(a) for a in input])}') #test assert = 2

def isSafeDamp(seq):
    for i in range(0,len(seq)):
        seq2 = seq.copy()
        del seq2[i]
        if isSafe(seq2) : return 1
    return 0

print(f'Part B: answer = {sum([isSafeDamp(a) for a in input])}') #test assert = 4