
def getSurfaceArea(l, w, h):
	return ((2 * l*w) + (2 * w*h) + (2 * h*l))


def getSlack(l, w, h):
	ascending = [int(x) for x in [l, w, h]]
	ascending.sort()
	return (int(ascending[0]) * int(ascending[1]))

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
	
	totalArea = 0

	for box in boxes:
		surfaceArea = getSurfaceArea(box[0], box[1], box[2])
		slack = getSlack(box[0], box[1], box[2])
		area = surfaceArea + slack

		totalArea = totalArea + area

	print(totalArea)

	file.close()


if __name__ == "__main__":
	main()