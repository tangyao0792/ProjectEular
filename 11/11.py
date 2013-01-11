f = open ( 'data.in' )

arr = []
# read data
while True:
	line = f.readline()
	length = len ( line )
	if length == 0:
		break
	
	tmp = map ( int, line.split() )
	arr.append(tmp)


ans = 1

dx = [0,1,1,-1]
dy = [1, 0, 1,1]
for i in range( 0, 20):
	for j in range( 0, 20):
		for k in range(0, 4):
			tmp = arr[i][j]
			nx = i
			ny = j
			flag = True
			for l in range(0, 3):
				nx = nx+dx[k]
				ny = ny+dy[k]
				if nx >= 20 or ny >=20 or nx <0 or ny < 0:
					flag = False
					break
				tmp = tmp * arr[nx][ny]

			if tmp > ans and flag:
				ans = tmp
	
print ans
