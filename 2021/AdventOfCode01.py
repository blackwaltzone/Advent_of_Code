datalist = []

with open("input01.txt") as file:
	for line in file:
		line = line.strip()
		datalist.append(int(line))
file.close()

# unit test
#datalist = [199,200,208,210,200,207,240,269,260,263]
count = 0
#i = 0

# Part 1 - First strategy
###for data in datalist:
###	if data != datalist[0]:
###		if data > datalist[i - 1]:
###			count += 1
###	i += 1

# Part 1 - Second strategy
###for i in range(len(datalist)):
###	if i != 0:
###		if datalist[i] > datalist[i - 1]:
###			count += 1

# Part 2
sum = 0
prevsum = 0

for i in range(len(datalist)):
	if (i + 3) <= len(datalist):
		for j in range(i, i + 3):
			sum += datalist[j]
		if i != 0:
			if sum > prevsum:
				count += 1
		prevsum = sum
		sum = 0
	else:
		break

print(f"Measurements: {count}")