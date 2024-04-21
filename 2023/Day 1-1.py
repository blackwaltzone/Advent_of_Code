
def concatenate(num1, num2):
	return int(f'{num1}{num2}')


def getValues(inputs):
	calibration_values = []

	for line in inputs:
		values = [int(i) for i in line if i.isdigit()]
		calibration_values.append([values[0],values[-1]])

	return calibration_values


def getSum(values):
	total = 0

	for item in values:
		line = concatenate(item[0],item[1])
		print(line)
		total = total + line

	return total




def main():
	file = open("input1.txt", "r")

	total_sum = getSum(getValues(file))

	file.close()

	print(total_sum)


if __name__ == "__main__":
	main()