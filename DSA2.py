def consec(n):
	z=str(n)
	y=len(z)
	sum=0
	for i in range(y-1):
		a= int(z[i])
		b= int(z[i+1])
		sum+=a*b
	print(sum)
	
n=23145
consec(n)