hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r= float(rate)
except:
    print("Enter Numeric values only")
    quit()
def computepay(h, r):
    if h>40 :
        pay=40*r+(h-40)*r*1.5
    else:
        pay=h*r
    return pay
p = computepay(h, r)
print("Pay", p)