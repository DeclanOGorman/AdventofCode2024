import re

with open('./3/input.txt', 'r') as f:
    input = f.read().strip()

sumA = 0; sumB = 0; enabled = True
for a in re.findall(r'mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don\'t\(\))', input):
    if a[0] == '' : enabled = (a[1] == 'do()')
    else :
        d = list(map(int, a[0].split(',')))
        sumA += d[0] * d[1]
        sumB += d[0] * d[1] if enabled == True else 0

print(f'Part A: answer = {sumA}') #test assert = 161
print(f'Part B: answer = {sumB}') #test assert = 48