sum = 0

f = []

f.append(1)
f.append(1)

while True:
	f[0] = f[0]+f[1]
	f[1] = f[0]+f[1]
	print f[0],f[1]
	if f[0] > 4000000:
		break
	if f[0] % 2 == 0:
		sum = sum + f[0]

	if f[1] > 4000000:
		break
	if f[1] % 2 == 0:
		sum = sum + f[1]
	
print sum
