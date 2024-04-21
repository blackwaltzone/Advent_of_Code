import sys
import hashlib

def find_leading_zeros(input_key: str, num_zeros: int) -> int:
    index = 1

    while True:
        key = input_key + str(index)
        digest = hashlib.md5(key.encode('ascii')).hexdigest()
        if digest[:num_zeros] == "0" * num_zeros:
            break
        index += 1
    return index
    

def solve1(path: str) -> None:
    with open(path) as f:
        data = f.read().strip()
    print(find_leading_zeros(data, 5))


def solve2(path: str) -> None:
    with open(path) as f:
        data = f.read().strip()
    print(find_leading_zeros(data, 6))


if __name__ == '__main__':
	n = int(sys.argv[1])
	path = sys.argv[2]

	if n == 1:
		solve1(path)
	elif n == 2:
		solve2(path)
