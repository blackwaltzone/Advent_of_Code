seats = []
checkSeats = []

for x in range(48,818):
	checkSeats.append(x)

with open("input5.txt") as file:
	for line in file:
		rawRow = line[:-4]
		rawCol = line[-4:]
		row = []
		col = []
		for x in rawRow:
			if x == "F":
				row.append(0)
			elif x == "B":
				row.append(1)
		for y in rawCol:
			if y == "L":
				col.append(0)
			elif y == "R":
				col.append(1)

		rowNum = 0
		colNum = 0
		rowNum += int(row[0]) * 64
		rowNum += int(row[1]) * 32
		rowNum += int(row[2]) * 16
		rowNum += int(row[3]) * 8
		rowNum += int(row[4]) * 4
		rowNum += int(row[5]) * 2
		rowNum += int(row[6]) * 1

		colNum += int(col[0]) * 4
		colNum += int(col[1]) * 2
		colNum += int(col[2]) * 1

		seatID = (rowNum * 8) + colNum

		seats.append(seatID)

		seats.sort()

	diff = [i for i in seats + checkSeats if i not in seats]
	print(diff)
file.close()