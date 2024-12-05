with open('./5/input.txt', 'r') as f:
    input = [a.strip() for a in f]

sets = [a.split(',') for a in input[input.index('')+1:]]
ruled = {}
for r in [a.split('|') for a in input[:input.index('')]]:
    ruled[r[0]] = ruled[r[0]] + [r[1]] if r[0] in ruled else [r[1]]

def checkSet(set) :
    for i in s :
        if i in ruled :
            for r in ruled[i]:
                if r in s and s.index(r) < s.index(i) :
                    return s.index(i), s.index(r)
    return -1, -1

mids = 0; invalidSet = []
for s in sets :
    i, j = checkSet(s)
    if i == -1 :
        mids += int(s[int((len(s)+1)/2)-1])
    else :
        invalidSet += [s]

print(f'Part A: answer = { mids }') #test assert = 143

mids = 0
for s in invalidSet :
    valid = False
    s2 = s
    while not valid :
        i, j = checkSet(s2)
        if i == -1 : valid = True
        else :
            si = s2[i]
            s2.remove(si)
            s2.insert(j, si)

    print(s2)
    mids += int(s[int((len(s)+1)/2)-1])

print(f'Part B: answer = { mids }') #test assert = 123