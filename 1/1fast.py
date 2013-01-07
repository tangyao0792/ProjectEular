def getSumOfMul( low, high, mul):
	low = low +( mul - low % mul )
	high = high - ( high % mul )
	times = ( high - low ) / mul + 1
	retVal = (low +high ) * times / 2
	return retVal

print getSumOfMul( 0, 999, 3) + getSumOfMul( 0, 999, 5) - getSumOfMul(0, 999, 15)

