name = input("Enter file:")
count=0
list1=list()
dict1=dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for lines in handle:
    if lines.startswith("From"):
        if lines.startswith("From:"):
            continue
        else:
            count=count+1
            line=lines.split()
            print(line)
            str1=''.join(line[5])
            list1.append(str1[0:2])
for word in list1:
    dict1[word]= dict1.get(word,0)
for k,v in sorted(dict1.items()):
    print(k,v)