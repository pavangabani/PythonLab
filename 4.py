import math
a=float(input("Enter a"))
b=float(input("Enter b"))
c=float(input("Enter c"))
d=b*b-4*a*c
if d<0:
	print("No Solution")
else:
	d=math.sqrt(d)
	print("Solution",(-b+d)/2*a,(-b-d)/2*a)
