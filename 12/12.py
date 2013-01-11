def getNumOfDivs(x):
	retVal = 1
	i = 2
	print x,
	while i <= x:
		count = 0
		while x % i == 0:
			count = count + 1
			x = x / i
		i = i + 1
		retVal = retVal * (count + 1)
	print retVal
	return retVal

if __name__ == "__main__":
	i = 1
	while True:
		x = i * (i + 1) / 2
		if getNumOfDivs(x) > 500:
			print x
			break
		i = i + 1
