text = "X-DSPAM-Confidence:    0.8475"
l=len(text)
for num in text:
    pos=text.find(":")
fnum=float(text[pos+1:l].strip())
print(fnum)