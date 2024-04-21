def get_data(datfile):
    raw_data = []

    with open(datfile) as file:
        for line in file:
            line = line.strip()
            raw_data.append(line)
    file.close()

    #all_lines = [[int(x) for x in line.strip()] for line in raw_data.readlines()]
    #return all_lines
    return raw_data

def get_drawn_numbers(data):
    return data.split(',')

def get_boards(data):
    board = []
    boards = []
    count = 0
    for line in data:
        line.strip()
        if line == '':
            continue
        else:
            formatted_line = line.split(' ')
            for item in formatted_line:
                if item == '':
                    formatted_line.remove(item)
            board.append(formatted_line)
            count += 1
        if count == 5:
            boards.append(board)
            board = []
            count = 0
    return boards

def draw_numbers(numbers, boards):
    for board in boards:
        for line in board:
            check = all(item in numbers for item in line)
            if check == True:
                return board
        for i in range(5):
            check = all(item in numbers for item in board[i])
            if check == True:
                return board                
    return None


raw_data = get_data("input04.txt")
drawn_numbers = get_drawn_numbers(raw_data[0])
boards = get_boards(raw_data[1:len(raw_data)])

sum_unmarked = 0
prev_drawn_numbers = []
for i in drawn_numbers:
    prev_drawn_numbers.append(i)
    winning_board = draw_numbers(prev_drawn_numbers, boards)
    if winning_board != None:
        winning_number = int(i)
        break

for line in winning_board:
    for item in line:
        if item not in prev_drawn_numbers:
            sum_unmarked += int(item)

score = winning_number * sum_unmarked

print(f"Winning score: {score}")