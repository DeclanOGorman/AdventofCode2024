with open('./9/input.txt', 'r') as f:
    input = list(map(int, list(f.readline().strip())))

# Len / ID
fsA = [(f, -1 if i % 2 == 1 else int(i / 2)) for i, f in enumerate(input)]
fsB = [(f, -1 if i % 2 == 1 else int(i / 2)) for i, f in enumerate(input)]

def defrag(fs, contiguous) :
    for fI, f in reversed(list(enumerate([f for f in fs if f[1] != -1]))) : 
                
        # get first free space
        sI = -1
        fI = fs.index(f)
        fileLen = f[0]
        for i, s in enumerate(fs) :
            if s[1] == -1 and (not contiguous or s[0] >= fileLen): 
                sI = i
                break

        # move file to free space, iterate if needed
        spaceLen = fs[sI][0]        
        if sI > fI : continue
        if fileLen < spaceLen : # Split space
            fs[sI] = (fileLen, f[1])
            fs[fI] = (fileLen, -1)
            fs.insert(sI+1,(spaceLen - fileLen, -1))
        elif fileLen == spaceLen :
            fs[sI] = (fs[sI][0],f[1])
            fs[fI] = (f[0],-1)
        else :
            fs[sI] = (fs[sI][0],f[1])
            fs[fI] = (f[0] - fs[sI][0], f[1])
            fs.insert(fI+1,(fileLen-spaceLen, -1))

        if sI % 500 == 0 :
            print(f'\rCompleted: {sI} of {len(fs)}', end = '\r')
        
    return fs

# calculate checksum
def checkSum(fs) :
    i = 0; sum = 0; lenFS = len(fs)
    for fI, f in enumerate(fs) :
        fileID = f[1]
        fileLen = f[0]

        for i2 in range(fileLen) :
            if fileID != -1 : sum += fileID * i
            i += 1
        
        if fI % 500 == 0 :
            print(f'\rCompleted: {fI} of {lenFS}', end = '\r')
    
    return sum

#Note Part A seems to be broken by fixes to Part B, not going back to fix..
print(f'Part A: answer = { checkSum(defrag(fsA, False)) }') #test assert = 1928
print(f'Part B: answer = { checkSum(defrag(fsB, True)) }') #test assert = 