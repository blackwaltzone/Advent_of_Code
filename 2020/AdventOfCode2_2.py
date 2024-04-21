

with open("input2.txt") as file:
	validCount = 0
	pos1 = 0
	pos2 = 0
	for line in file:
		counter = 0
		offset = 0
		dash = line.find("-")
		password = line.find(":")
		space = line.find(" ")
		min1 = (line[:dash])
		max1 = (line[dash+1:dash+3])

		keyLetter = line[password - 1:password]
		password = line[password+1:]

		pos1 = int(min1)
		pos2 = int(max1)

		if password[pos1] != password[pos2]:
			if password[pos1] == keyLetter:
				validCount += 1
			elif password[pos2] == keyLetter:
				validCount += 1

file.close()

print(validCount)