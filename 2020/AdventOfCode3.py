grid = []
treeCount1 = 0
treeCount2 = 0
treeCount3 = 0
treeCount4 = 0
treeCount5 = 0
pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0
pos5 = 0
pos5v = 0
increment1 = 1
increment2 = 3
increment3 = 5
increment4 = 7
increment5 = 1
verticalIncrement5 = 2

numRows = 0
numCols = 0

with open("input3.txt") as file:
	for line in file:
		line = line.strip()
		grid.append(line)
file.close()

numRows = len(grid)
numCols = len(grid[0])

for line in grid:
	if pos1 >= numCols:
		offset = pos1 - numCols
		pos1 = offset
	if pos2 >= numCols:
		offset = pos2 - numCols
		pos2 = offset
	if pos3 >= numCols:
		offset = pos3 - numCols
		pos3 = offset
	if pos4 >= numCols:
		offset = pos4 - numCols
		pos4 = offset
	if pos5 >= numCols:
		offset = pos5 - numCols
		pos5 = offset

	if line[pos1] == "#":
		treeCount1 += 1
	if line[pos2] == "#":
		treeCount2 += 1
	if line[pos3] == "#":
		treeCount3 += 1
	if line[pos4] == "#":
		treeCount4 += 1
	if line[pos5] == "#":
		if pos5v % 2 == 0:
			treeCount5 += 1
		pos5 += increment5

	pos1 += increment1
	pos2 += increment2
	pos3 += increment3
	pos4 += increment4
	pos5v += 1

multiple = treeCount1 * treeCount2 * treeCount3 * treeCount4 * treeCount5
print(multiple)