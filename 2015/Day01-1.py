
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


def getFloor(directions):
	floor = 0

	for item in directions:
		floor = floor + getMove(item)

	return floor


def main():

	file = open("input1.txt", "r")
	values = parseInput(file)

	floor = getFloor(values)
	print(floor)

	file.close()


if __name__ == "__main__":
	main()