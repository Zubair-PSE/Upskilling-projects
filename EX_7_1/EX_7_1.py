import os
os.system('cls')

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Enter valid file name')
    quit()
for line in fh:
    line=line.upper()
    print(line.strip())