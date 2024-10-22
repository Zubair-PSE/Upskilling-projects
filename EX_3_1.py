import os
os.system('cls')
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r= float(rate)
except:
    print("Enter Numeric values only")
    quit()
pay=0
if h>40 :
    pay=40*r+(h-40)*r*1.5
else:
    pay=h*r
print (pay)