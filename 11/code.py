with open('./11/input.txt', 'r') as f:
    input = list(map(int,f.readline().strip().split(' ')))

stones = dict()
for s in input : 
    stones[s] = 1

def addorUpdate(d, key, value) : #I feel like there should be a better way to do this
    dict.setdefault(d,key,0)
    d[key] += value

def blink(d) :
    newS = dict()
    for i in d :
        if i == 0 :
            addorUpdate(newS,1,d[i])
        elif len(str(i)) % 2 == 0 :
            addorUpdate(newS,int(str(i)[:len(str(i))//2]), d[i])
            addorUpdate(newS,int(str(i)[len(str(i))//2:]), d[i])
        else :
            addorUpdate(newS,i*2024,d[i])
    return newS

def runBlinks(s, n) :
    for b in range(n) :
        s = blink(s)
    return s    

print(f'Part A: answer = { sum(list(runBlinks(stones,25).values())) }') #test assert = 
print(f'Part B: answer = { sum(list(runBlinks(stones,75).values())) }') #test assert = 