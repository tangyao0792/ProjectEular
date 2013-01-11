def gcd ( a, b):
	if a % b == 0:
		return b
	return gcd( b, a%b)


ans = 1

for i in range ( 1, 21 ):
	if ans % i == 0:
		continue
	else:
		ans = ans * ( i / gcd ( ans, i) )

print ans
