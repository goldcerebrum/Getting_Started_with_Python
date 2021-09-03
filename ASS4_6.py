def computepay(h, r):
	if h > 40 :
		th = h-40
		rh = 40
		rr = r*1.5
		p = rh*r+th*rr
	else :
		p = h*r
	return p

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
