datalist = []

with open("input.txt") as file:
	for line in file:
		line = line.strip()
		datalist.append(int(line))
file.close()

for i in datalist:
	for j in datalist:
		for k in datalist:
			if i + j + k == 2020:
				print (i * j * k)
				quit()