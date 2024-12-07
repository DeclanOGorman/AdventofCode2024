with open('./6/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

dirs = [[-1,0],[0,1],[1,0],[0,-1]]
gX = -1; gY = -1; max = len(input)
for i in range(len(input)) :
    if '^' in input[i] :
        gY = i
        gX = input[i].index('^')

def runSearch(grid, x, y, bX, bY) :
    pos = set(); posdir = set(); dir = 0; steps = 0
    while x >= 0 and y >= 0 and x < max and y < max :
        if (x,y) not in pos : pos.add((x,y))
        if (x,y,dir) in posdir : return {}

        posdir.add((x,y,dir))

        x2 = x+dirs[dir][1]
        y2 = y+dirs[dir][0]

        while (x2 >= 0 and y2 >= 0 and 
            x2 < max and y2 < max and
            (input[y2][x2] == '#' or
            (x2 == bX and y2 == bY))) :
            dir = (dir + 1) % 4
            x2 = x+dirs[dir][1]
            y2 = y+dirs[dir][0]
        
        x = x2; y = y2
    return pos

pos = runSearch(input,gX,gY,-1,-1)
print(f'Part A: answer = { len(pos) }') #test assert = 41
print(f'Part B: answer = { sum([1 for (x,y) in pos if len(runSearch(input, gX, gY, x, y)) == 0]) }') #test assert = 6