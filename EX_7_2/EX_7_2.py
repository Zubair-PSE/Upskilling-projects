# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find(':')
    line=line[pos+1:].strip()
    fline=float(line)
    #print(fline)
    count=count+1
    tot=tot+fline
    avg=tot/count 
print('Average spam confidence:',avg)
#print("Done")