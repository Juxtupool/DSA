def corres(n,k):
	sum1=0

	while(n>0 and k>0):
		sum1+= ((n %10) * (k%10))
		n=n//10
		k=k//10
	print(sum1)



n= 327
k=539
corres(n,k)