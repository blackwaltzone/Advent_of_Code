def isHouseRepeated(pos):
	pass


def houseCrawl(directions):
	position = (0,0)
	locations = [position]
	for step in directions:
		new_position = direction(step)
		position = (position[0] + new_position[0], position[1] + new_position[1])
		#print(position)
		if not position in locations:
			locations.append(position)

	return locations


def parseInput(rawInput):
	list = []
	for line in rawInput:
		for item in line:
			list.append(item)
	return list


def direction(dir):
	if dir == '>':
		return (1,0)
	elif dir == '<':
		return (-1,0)
	elif dir == '^':
		return (0,1)
	else:
		return (0,-1)	


def main():
	input1 = ">"
	input2 = "^>V<"
	input3 = "^V^V^V^V^V"
	input4 = ">>^^^<<^VVV><><^VVVV<>^"

	file = open("input3.txt", "r")
	directions = parseInput(file)

	houses = houseCrawl(directions)
	print(len(set(houses)))


if __name__ == "__main__":
	main()