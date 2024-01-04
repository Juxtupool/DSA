def rev(n):
	while n:
		print(n%10, end='')
		n=n//10

n=1234
rev(n)