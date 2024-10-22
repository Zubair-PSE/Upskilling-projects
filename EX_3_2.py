score = input("Enter Score: ")

try:
    s= float(score)
except:
    print("Enter number values only")
    quit()
if s>=.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    prnit("D")
elif s<0.6:
    print ("F")
else:
    print ("Number out of range")