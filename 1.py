def isprime(num):
	i = 2
	while(i<num):
		if num%i==0:
			return False
		i += 1
	return True

def goldbachresolve(num):
	for i in range(2,num):
		if isprime(i) and isprime(num-i):
			print(num,'=',i,'+',num-i)
			return True
	return False
times=10000
i=4
while(goldbachresolve(i) and i<times):
	i += 2
if i==times:
	print("Goldbach hypothesis is proven in the given range.")
else:
	print("Goldbach hypothesis is proven wrong!")
