def pos(n):
	power=0
	while n>0:
		x= (n%10)*(10**power)
		n=n//10
		power+=1
		print(x, end=",")

n=21463
pos(n)