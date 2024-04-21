

with open("input2.txt") as file:
	validCount = 0
	min = 0
	max = 0
	for line in file:
		counter = 0
		offset = 0
		dash = line.find("-")
		password = line.find(":")
		space = line.find(" ")
		min = (line[:dash])
		max = (line[dash+1:dash+3])

		keyLetter = line[password - 1:password]
		password = line[password+1:]

		for i in password:
			if i == keyLetter:
				counter+=1

		if counter <= int(max):
			if counter >= int(min):
				validCount += 1
file.close()

print(validCount)