
def getBow(l, w, h):
	return (l * w * h)


def getWrap(l, w, h):
	ascending = [int(x) for x in [l, w, h]]
	ascending.sort()
	return (2 * int(ascending[0]) + 2 * int(ascending[1]))

def parseInput(rawInput):
	boxes = []
	for line in rawInput:
		dimensions = line.split('x')
		dimensions[2] = dimensions[2].strip()
		dimensions[0] = int(dimensions[0])
		dimensions[1] = int(dimensions[1])
		dimensions[2] = int(dimensions[2])
		boxes.append(dimensions)

	return boxes



def main():

	file = open("input2.txt", "r")
	boxes = parseInput(file)

	#boxes = [(2, 4, 3), (10, 1, 1)]
	
	totalRibbon = 0

	for box in boxes:
		wrap = getWrap(box[0], box[1], box[2])
		bow = getBow(box[0], box[1], box[2])
		boxRibbon = wrap + bow
		#print(boxRibbon)

		totalRibbon = totalRibbon + boxRibbon

	print(totalRibbon)

	file.close()


if __name__ == "__main__":
	main()