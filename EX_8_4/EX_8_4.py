fname = input("Enter file name: ")
fh = open(fname)
lst = list()
w=list()
for line in fh:
    for w in line.split():
        if w in lst:
            continue
        else:
            lst.append(w)
lst.sort()
print(lst)