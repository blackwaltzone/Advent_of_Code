import sys
from collections import Counter

def vowels(input):
    list = ['a', 'e', 'i', 'o', 'u']
    total = 0

    for char in input:
        if char in list:
            total += 1

    if total < 3:
        return False
    else:
        return True


def duplicates(input):
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            return True
    return False


def findbadletters(input):
    list = ['ab', 'cd', 'pq', 'xy']
    for value in list:
        if value in input:
            return False
    return True

def twopairs(input):
    for i in range(len(input)-1):
        pair = input[i] + input[i+1]
        count = input.count(pair)
        if count >= 2:
            return True
    return False


def repeat(input):
    for i in range(len(input)-2):
        if input[i] == input[i+2]:
            return True
    return False


def getlines(input):
    return input.splitlines()


def solve1(path: str) -> None:
    with open(path) as f:
        data = f.read().strip()

    nicelines = []

    lines = getlines(data)
    #lines = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
    for line in lines:
        if vowels(line) and duplicates(line) and  findbadletters(line):
            nicelines.append(line)
    print(len(nicelines))



def solve2(path: str) -> None:
    with open(path) as f:
        data = f.read().strip()

    nicelines = []
    lines = getlines(data)
    #lines = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazuczvgmuy']

    for line in lines:
        if twopairs(line) and repeat(line):
            nicelines.append(line)
    print(len(nicelines))


if __name__ == '__main__':
	n = int(sys.argv[1])
	path = sys.argv[2]

	if n == 1:
		solve1(path)
	elif n == 2:
		solve2(path)
