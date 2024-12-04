with open('./4/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

word = ['X','M','A','S']
dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

def limit(x, y, b) : #Assumes square input
    return x < 0+b or x >= len(input)-b or y < 0+b or y >= len(input)-b

def search(grid, i, j) :
    x = i; y = j; sum = 0
    for d in dirs :
        for wi in range(len(word)) :
            if (limit(x+d[0]*wi,y+d[1]*wi, 0) or
                grid[x+d[0]*wi][y+d[1]*wi] != word[wi]) :
                break
            elif wi == len(word)-1 : 
                sum += 1
    return sum

sumA = 0; sumB = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == word[0] :
            sumA += search(input, i, j)

print(f'Part A: answer = { sumA }') #test assert = 18

def searchMas(grid, x, y) :
    x = i; y = j; sum = 0
    return 1 if (((grid[x-1][y-1] == 'M' and grid[x+1][y+1] == 'S') or
        (grid[x-1][y-1] == 'S' and grid[x+1][y+1] == 'M')) and
        ((grid[x+1][y-1] == 'M' and grid[x-1][y+1] == 'S') or
        (grid[x+1][y-1] == 'S' and grid[x-1][y+1] == 'M'))) else 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'A' and not limit(i,j,1):
            sumB += searchMas(input, i, j)

print(f'Part B: answer = { sumB }') #test assert = 9