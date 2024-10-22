score = input("Enter Score: ")
try:
    s= float(score)
except:
    print("Enter number values only")
    quit()
if s>1 or s<0:
    print("Number out of range")
elif s>=.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
elif s<0.6:
    print ("F")