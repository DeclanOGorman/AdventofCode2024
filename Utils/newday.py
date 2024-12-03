import shutil

day = 3

# Copy file to new directory and rename it
shutil.copyfile('./Template/code.py', f'./{day}/code.py')
shutil.copyfile('./Template/test.txt', f'./{day}/test.txt')
shutil.copyfile('./Template/input.txt', f'./{day}/input.txt')

# Open file, find and replace text
with open(f'./{day}/code.py', 'r') as file:
    filedata = file.read().replace('/X/', f'/{day}/')

with open(f'./{day}/code.py', 'w') as file:
    file.write(filedata)