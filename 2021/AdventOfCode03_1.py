
def convert_bin_to_dec(num):
    return sum(2**pos*value for pos, value in enumerate(num))

raw_datalist = []

#with open("input03.txt") as file:
#	for line in file:
#		line = line.strip()
#		raw_datalist.append(line)
#file.close()

raw_datalist = ['00100',
                '11110',
                '10110',
                '10111',
                '10101',
                '01111',
                '00111',
                '11100',
                '10000',
                '11001',
                '00010',
                '01010']

str_len = int(len(raw_datalist[0]))

counts_1 = [0 for i in range(str_len)]
counts_0 = [0 for i in range(str_len)]

for x in raw_datalist:
    i = 0
    for y in x:
        if x[i] == '1':
            counts_1[i] += 1
        elif x[i] == '0':
            counts_0[i] += 1
        i += 1
    i = 0

gamma_bin = [0 for i in range(str_len)]
epsilon_bin = [0 for i in range(str_len)]

for x in range(str_len):
    if counts_1[x] > counts_0[x]:
        gamma_bin[x] = 1
        epsilon_bin[x] = 0
    else:
        gamma_bin[x] = 0
        epsilon_bin[x] = 1

gamma_dec = convert_bin_to_dec(gamma_bin[::-1])
epsilon_dec = convert_bin_to_dec(epsilon_bin[::-1])

power_consumption = gamma_dec * epsilon_dec

print(power_consumption)