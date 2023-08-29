def LifeGrid(nrows, ncols): #tao ra mot hinh chu nhat (luoi) voi tat ca cac cell deu dead
	grid = [[0]*ncols for x in range(nrows)]
	return grid

def numRows(): #return nrows
	nrows = input("Enter the number of rows (>=4): ")
	return int(nrows)

def numCols(): #return ncols
	ncols = input("Enter the number of columns (>=4): ")
	return int(ncols)

def configure(coordList): #Ham khoi tao the he: doi so coordList la chuoi cac 2-tuple, moi tuple chua toa do cua cell can khoi tao la alive, nhung cell con lai khoi tao la dead 
	for i in coordList:
		setCell(i[0], i[1])

def clearCell(row, col): #set a sell to dead
	grid[row-1][col-1] = 0

def setCell(row, col): #set a sell to be alive
	grid[row-1][col-1] = 1

def isLiveCell(row, col): #kiem tra mot cell dang alive (True) hay dead (False)
	if grid[row-1][col-1] == 1:
		return True
	else: return False

def numLiveNeighbors(row, col): #Return so hang xom dang alive cua mot cell
	numLiveNbs = 0
	row -= 1
	col -= 1
	try:
		if grid[row-1][col-1] == 1 and row-1 >= 0 and col-1 >=0:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	try:
		if grid[row-1][col] == 1 and row-1 >= 0:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	try:
		if grid[row-1][col+1] == 1 and row-1 >= 0:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	try:
		if grid[row][col-1] == 1 and col-1 >= 0:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	try:
		if grid[row][col+1] == 1:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	try:
		if grid[row+1][col-1] == 1 and col-1 >= 0:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	try:
		if grid[row+1][col] == 1:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	try:
		if grid[row+1][col+1] == 1:
			numLiveNbs += 1
	except:
		numLiveNbs += 0
	return numLiveNbs

def draw(grid):
	for i in grid:
		for j in i:
			print(j, end=" ")
		print()

def nextgen():
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if isLiveCell(i+1, j+1):
				if numLiveNeighbors(i+1, j+1) == 2 or numLiveNeighbors(i+1, j+1) == 3:
					try:
						coordList.remove((i+1,j+1))
						coordList.append((i+1,j+1))
					except:
						coordList.append((i+1,j+1))
				elif numLiveNeighbors(i+1, j+1) <= 1 or numLiveNeighbors(i+1, j+1) >= 4:
					coordList.remove((i+1, j+1))
			else:
				if numLiveNeighbors(i+1, j+1) == 3:
					coordList.append((i+1,j+1))

#KHOI TAO
gen_number = 0
nrows = numRows()
ncols = numCols()
grid = LifeGrid(nrows, ncols)
coordList = [(1,2), (1,3), (1,4), (4,2), (4,3), (4,4)]
configure(coordList)
print("Gen 0:")
draw(grid)

while True:
	if len(coordList) == nrows*ncols:
		print("All organisms be alive, it's the eternal grid")
		break
	elif len(coordList) == 0:
		print("All organisms died")
		break
	else:
		temp = input("Enter any character to show next gen, but type 'e' to end program: ")
		if temp == 'e':
			break
	gen_number += 1
	print("Gen " + str(gen_number) + ":")
	nextgen()
	grid = LifeGrid(nrows, ncols)
	configure(coordList)
	draw(grid)