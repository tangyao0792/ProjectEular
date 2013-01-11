nmax =10 

notprime = [0] * (nmax+1)


for i in range(2, nmax+1):
	if notprime[i] == 1:
		continue
	print i
	j = 2
	while True:
		if i * j > nmax:
			break
		notprime[i*j]=1
		j = j + 1

sum = 0
for i in range(2,nmax + 1):
	if notprime[i] == 0:
		sum = sum + i

print sum
