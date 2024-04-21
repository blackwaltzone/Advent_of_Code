
#test_string1 = ["(())","()()"]		# "0"
#test_string2 = ["(((","(()(()("]	# "3"
#test_string3 = ["())","))("]		# "-1"


def getMove(dir):
	if dir == "(":
		return int(1)
	elif dir == ")":
		return int(-1)

	return int(0)


def parseInput(rawInput):
	inputs = []
	for line in rawInput:
		for char in line:
			inputs.append(char)

	return inputs


def getPosition(directions):
	floor = 0
	position = 1

	for item in directions:
		floor = floor + getMove(item)

		if floor == -1:
			return position
		else:
			position = position + 1

	return position


def main():

	file = open("input1.txt", "r")
	values = parseInput(file)

	pos = getPosition(values)
	print(pos)

	file.close()


if __name__ == "__main__":
	main()