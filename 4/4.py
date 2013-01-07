def isPalindrome ( x ):
	strx = str ( x )
	l = 0
	r = len( strx ) - 1

	while l <= r:
		if strx[l] != strx[r]:
			return False
		l = l + 1
		r = r - 1

	return True

ans = 0

for i in range ( 100, 1000):
	for j in range ( 100, 1000):
		x = i * j
		if isPalindrome( x ):
			print x
			if x > ans:
				ans = x

print 'ans=',ans
