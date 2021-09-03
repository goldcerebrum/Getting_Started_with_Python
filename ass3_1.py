hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40 :
    th = h-40
    rh = 40
    rr = r*1.5
    print (rh*r+th*rr)
else :
    print (h*r)
    
