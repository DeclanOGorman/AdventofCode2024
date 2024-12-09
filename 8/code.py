with open('./8/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

def inBounds(n, max) : # Assumes square
    return (n[0] >= 0 and n[0] < max and 
            n[1] >= 0 and n[1] < max)

ant = dict()
for y, a in enumerate(input) :
    for x, b in enumerate(a) :
        if b == '.' : continue
        if b in ant : 
            ant[b] += [(x,y)]
        else :
            ant[b] = [(x,y)]

nodesA = set(); nodesB = set(); max = len(input)
for a in ant :
    for n1 in ant[a] :
        for n2 in ant[a] :
            if n1 == n2 : continue
            antinode = (n1[0]-n2[0]+n1[0], n1[1]-n2[1] + n1[1])
            if inBounds(antinode, max) :
                nodesA.add(antinode)

            nodesB.add(n2)
            while inBounds(antinode, max) :
                nodesB.add(antinode)
                antinode = (n1[0]-n2[0]+antinode[0], n1[1]-n2[1] + antinode[1])

print(f'Part A: answer = { len(nodesA) }') #test assert = 14
print(f'Part B: answer = { len(nodesB) }') #test assert = 34