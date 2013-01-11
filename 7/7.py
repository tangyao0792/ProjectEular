def isPrime ( x ):
	if x % 2 == 0 and x != 2:
		return False
	
	i = 3
	while True:
		if i * i > x:
			break
		if x % i == 0:
			return False
		i = i+2
	
	return True

cnt = 0

i = 2

while True:
	if isPrime(i):
		cnt = cnt + 1
		print i
	if cnt == 10001:
		break
	i = i + 1

print i
