with open('./12/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

map = dict()
for y, row in enumerate(input) : 
    for x, cell in enumerate(row) :
        map[cell] = map.get(cell, []) + [(x,y)]

def getNeighbours(x,y) :
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

def subVector(a,b) :
    return (a[0]-b[0],a[1]-b[1])

def addVector(a,b) :
    return (a[0]+b[0],a[1]+b[1])

def multVectorScalar(a,s) :
    return (a[0]*s,a[1]*s)

regions = dict()
for m in map :
    regions[m] = []
    while len(map[m]) > 0 :
        cell = map[m].pop()
        r = [cell]
        q = [cell]
        while len(q) > 0 :
            cell = q.pop()
            for n in getNeighbours(cell[0],cell[1]) :
                if n in map[m] :
                    map[m].remove(n)
                    r.append(n)
                    q.append(n)
        regions[m].append(r)

def calcFencing(region) :
    perim = 0; sides = 0; fVectors = []
    for c in region :
        for n in getNeighbours(c[0],c[1]) :
            if n not in region :
                fVectors += [(c,n)]
                perim += 1

    while len(fVectors) > 0 :
        v = fVectors.pop()
        sides += 1
        dir = subVector(v[0], v[1])
        dir = (dir[1],dir[0])
        for i in [-1,1] : 
            dist = i
            while True :
                d2 = multVectorScalar(dir,dist)
                f = (addVector(v[0], d2), 
                    addVector(v[1], d2))
                if f in fVectors :
                    fVectors.remove(f)
                    dist += i
                else:
                    break

    return perim * len(region), sides * len(region)

fencing = [calcFencing(r) for rS in regions for r in regions[rS] ]
print(f'Part A: answer = { sum([f[0] for f in fencing]) }') #test assert = 1930
print(f'Part B: answer = { sum([f[1] for f in fencing]) }') #test assert = 1206