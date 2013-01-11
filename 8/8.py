# wrong answer, don't understand the mean of problem
f = open ( 'data.in' )

arr = []
n , m = 0, 0

# read data
while True:
	line = f.readline()
	length = len ( line )
	if length == 0:
		break
	
	m = length - 1
	n = n + 1
	
	tmp = []

	for i in range ( 0, length-1):
		tmp.append(int(line[i]))
		
	arr.append(tmp)

print 'n = ',n,'	m = ',m


dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,1,-1,0,1,-1]

vis = []

def dfs( x, y, d ):
	if (x,y) in vis :
		return 0
	if d == 0:
		return 1
	
	vis.append((x,y))
	tans = 1

	for i in range(0, 8):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if nx >=n or ny >=m or nx<0 or ny<0:
			continue

		tmp = dfs(nx, ny, d-1)
		if tmp > tans:
			tans = tmp
	
	vis.remove((x,y))
	
	return tans * arr[x][y]
	

print dfs(0,0,5)

ans = 0

for i in range(0, n):
	for j in range(0, m):
		vis = []
		tmp = dfs( i, j, 5)
	#	print tmp," ",
		if tmp > ans:
			ans = tmp
	print ""

print ans 

