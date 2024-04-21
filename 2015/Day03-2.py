
def houseCrawl(directions):
	santa_pos = robo_pos = (0,0)
	count = 1
	santa = robo = [(0,0)]
	for step in directions:
		new_pos = direction(step)
		if count % 2 == 0:
			santa_pos = (santa_pos[0] + new_pos[0], santa_pos[1] + new_pos[1])
			santa.append(santa_pos)
		else:
			robo_pos = (robo_pos[0] + new_pos[0], robo_pos[1] + new_pos[1])
			robo.append(robo_pos)

		count += 1

	locations = set(santa+robo)

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