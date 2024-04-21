import sys

test_grid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]

grid = [[0 for col in range(1000)] for row in range(1000)]

def print_grid() -> None:
    for row in grid:
        for element in row:
            print(element, end=' ')
        print()


def count_lights() -> int:
    count = 0
    for row in grid:
        for element in row:
            if element == 1:
                count += 1
    return count


def count_brightness() -> int:
    brightness = 0
    for x in range(1000):
        for y in range(1000):
            brightness = brightness + grid[y][x]
    return brightness


def turn_on(start: int, stop: int) -> None:
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            if grid[y][x] == 0: 
                grid[y][x] = 1


def turn_on_2(start: int, stop: int) -> None:
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            grid[y][x] = grid[y][x] + 1


def toggle(start: int, stop: int) -> None:
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            if grid[y][x] == 0:
                grid[y][x] = 1
            else:
                grid[y][x] = 0


def toggle_2(start: int, stop: int) -> None:
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            grid[y][x] = grid[y][x] + 2


def turn_off(start: int, stop: int) -> None:
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            if grid[y][x] == 1:
                grid[y][x] = 0


def turn_off_2(start: int, stop: int) -> None:
    for x in range(start[0], stop[0] + 1):
        for y in range(start[1], stop[1] + 1):
            if grid[y][x] > 1:
                grid[y][x] = grid[y][x] - 1


def get_lines(input):
    return input.splitlines()
   

def read_line(raw_line):
    line = raw_line.split(' ')
    return line



def solve1(path: str) -> None:
    with open(path) as f:
        data = f.read().strip()
    instructions = get_lines(data)

    #print_grid()
    for raw_line in instructions:
        line = read_line(raw_line)

        if line[0] == 'toggle':
            start = tuple(map(int, line[1].split(',')))
            stop = tuple(map(int, line[3].split(',')))
            toggle(start, stop)
        else:
            start = tuple(map(int, line[2].split(',')))
            stop = tuple(map(int, line[4].split(',')))

            if line[1] == 'on':
                turn_on(start, stop)
            elif line[1] == 'off':
                turn_off(start, stop)

    lights = count_lights()
    #print_grid()
    print(f"Number of lights on: {lights}")


def solve2(path: str) -> None:
    with open(path) as f:
        data = f.read().strip()
    instructions = get_lines(data)

    for raw_line in instructions:
        line = read_line(raw_line)

        if line[0] == 'toggle':
            start = tuple(map(int, line[1].split(',')))
            stop = tuple(map(int, line[3].split(',')))
            toggle_2(start, stop)
        else:
            start = tuple(map(int, line[2].split(',')))
            stop = tuple(map(int, line[4].split(',')))

            if line[1] == 'on':
                turn_on_2(start, stop)
            elif line[1] == 'off':
                turn_off_2(start, stop)

    brightness = count_brightness()
    print(f"Total brightness: {brightness}")


if __name__ == '__main__':
	n = int(sys.argv[1])
	path = sys.argv[2]

	if n == 1:
		solve1(path)
	elif n == 2:
		solve2(path)
