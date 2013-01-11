f = open ("data.in")

arr = []

while True:
	line = f.readline()
	if len ( line ) == 0:
		break

	length = len (line)
	for i in range(0, length - 1 ):
		arr.append( int(line[i]) )

ans = 1

for i in range(0, 995):
	tmp = 1
	for j in range (0, 5):
		tmp = tmp * arr[i+j]
	
	if ans < tmp:
		ans = tmp

print ans
