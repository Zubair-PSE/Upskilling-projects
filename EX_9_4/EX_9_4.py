name = input("Enter file:")
count=dict()
bigmailer=None
bigcount=None
mails=[]
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
# To read each line from txt file 
for lines in handle:
    if lines.startswith('From:'):
        line=lines.split()
        mails.append(line[1]) #store the emails in which is in the 2nd place as list mails
#To read all the eamils and check for the biggest email sender and store as dictionary with its freq
for mail in mails: 
    count[mail]=count.get(mail,0)+1
# To chck for max sender and printit
for mail,c in count.items():
    if bigcount is None or c > bigcount:
        bigmailer=mail
        bigcount=c
print(bigmailer, bigcount)