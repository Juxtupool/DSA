def evnodsum(n):
	odd=0
	even=0
	while n>0:
		x=n%10
		if x%2:
			even+=x
		else:
			odd+=x
		n=n//10
	print('Sum of odd nos:',odd,',','Sum of even nos:',even)



n=23617
evnodsum(n)