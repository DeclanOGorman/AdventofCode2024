with open('./10/input.txt', 'r') as f:
    input = [list(map(int,list(a.strip()))) for a in f]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def inBounds(map, pos) :
    return pos[0] >=0 and pos[1] >= 0 and pos[0] < len(map) and pos[1] < len(map[0])

def walkMap(map, loc, h = 0) :

    peaks = []
    if map[loc[1]][loc[0]] == 9 :
        peaks.append(loc)

    for d in dirs :
        newLoc = (loc[0]+d[0], loc[1]+d[1])
        if inBounds(map, newLoc) and map[newLoc[1]][newLoc[0]] == h+1 and h <= 9:
            peaks += walkMap(map, newLoc, h+1)
                  
    return peaks

peaksA = sum([len(set(walkMap(input, (x,y)))) for y in range(len(input)) 
             for x in range(len(input[0])) if input[y][x] == 0])

peaksB = sum([len(walkMap(input, (x,y))) for y in range(len(input)) 
             for x in range(len(input[0])) if input[y][x] == 0])

print(f'Part A: answer = { peaksA }') #test assert = 
print(f'Part B: answer = { peaksB }') #test assert = 