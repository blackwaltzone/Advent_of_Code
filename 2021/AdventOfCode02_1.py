raw_datalist = []

with open("input02.txt") as file:
	for line in file:
		line = line.strip()
		raw_datalist.append(line)
file.close()

forward = 0
down = 0

#raw_datalist = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
data_dict = []

for line in raw_datalist:
    data = line.split(" ")
    direction = data[0]
    value = data[1]
    data_dict.append([direction, int(value)])

for i in data_dict:
    if i[0] == "forward":
        forward += i[1]
    elif i[0] == "down":
        down += i[1]
    elif i[0] == "up":
        down -= i[1]

total_return = forward * down

print(total_return)