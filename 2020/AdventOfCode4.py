passportDict = []
entry = {}
validCount = 0
counter = 0
minCount = 7

with open("input4.txt") as file:
	for line in file:
		if line != "\n":
			line = line.strip()
			line = line.split(" ")
			for x in line:
				if "byr" in x:
					entry["byr"] = x[x.index(":")+1:]
				if "iyr" in x:
					entry["iyr"] = x[x.index(":")+1:]
				if "eyr" in x:
					entry["eyr"] = x[x.index(":")+1:]
				if "hgt" in x:
					entry["hgt"] = x[x.index(":")+1:]
				if "hcl" in x:
					entry["hcl"] = x[x.index(":")+1:]
				if "ecl" in x:
					entry["ecl"] = x[x.index(":")+1:]
				if "pid" in x:
					entry["pid"] = x[x.index(":")+1:]
				if "cid" in x:
					entry["cid"] = x[x.index(":")+1:]
		else:# line == "\n":
			passportDict.append(entry)
			count = 0
			print(entry)
			if "byr" in entry:
				val = entry["byr"]
				valLen = len(val)
				val = int(val)
				if valLen == 4 and val >= 1920 and val <= 2002:
					print("byr valid")
					count += 1
				else:
					print("byr INVALID")
			else:
				print("no byr")
			if "iyr" in entry:
				val = entry["iyr"]
				valLen = len(val)
				val = int(val)
				if valLen == 4 and val >= 2010 and val <= 2020:
					print("iyr valid")
					count += 1
				else:
					print("iyr INVALID")
			else:
				print("no iyr")
			if "eyr" in entry:
				val = entry["eyr"]
				valLen = len(val)
				val = int(val)
				if valLen == 4 and val >= 2020 and val <= 2030:
					print("eyr valid")
					count += 1
				else:
					print("eyr INVALID")
			else:
				print("no eyr")
			if "hgt" in entry:
				item = entry["hgt"]
				unit = item[-2:]
				val = item[:-2]
				if val.isdigit():
					val = int(val)
				if unit == "cm":
					if val >= 150 and val <= 193:
						print("height cm valid")
						count += 1
					else:
						print("height out of range cm")
				elif unit == "in":
					if val >= 59 and val <= 76:
						print("height in valid")
						count += 1
					else:
						print("height out of range in")
				else:
					print("hgt INVALID")
			else:
				print("no hgt")
			if "hcl" in entry:
				item = entry["hcl"]
				if item[0] == "#":
					val = item[1:]
					if len(item) == 7:
						print("hcl valid")
						count += 1
					else:
						print("hcl INVALID wrong length")
				else:
					print("hcl INVALID no pound sign")
			else:
				print("no hcl")
			if "ecl" in entry:
				val = entry["ecl"]
				if val == "amb" or val == "blu" or val == "brn" or val == "gry" or val == "grn" or val == "hzl" or val == "oth":
					print("ecl valid")
					count += 1
				else:
					print("ecl INVALID")
			else:
				print("no ecl")
			if "pid" in entry:
				val = entry["pid"]
				#val = int(val)
				if len(val) == 9:
					if val.isdigit():
						print("pid valid")
						count += 1
					else:
						print("pid INVALID not a digit")
				else:
					print("pid INVALID wrong length")
			else:
				print("no pid")

			if count >= minCount:
				validCount += 1
				print("counted")
			else:
				print("not counted")

			entry = {}
file.close()

print(validCount)