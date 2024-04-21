def get_data(datfile):
    raw_data = []

    with open(datfile) as file:
        for line in file:
            line = line.strip()
            raw_data.append(line)
    file.close()

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
            board.append(list(map(int, formatted_line)))
            count += 1
        if count == 5:
            boards.append(board)
            board = []
            count = 0
    return boards

def score(board):
    total = 0
    for row in board:
        for number in row:
            if int(number) > 0:
                total += int(number)
    return total

def check_board(board):
    boardT = tuple(zip(*board))
    NEG_SET = set([-1])
    for i in range(len(board)):
        if set(board[i]) == NEG_SET or set(boardT[i]) == NEG_SET:
            return True
    return False

raw_data = get_data("input04.txt")
numbersList = get_drawn_numbers(raw_data[0])
boards = get_boards(raw_data[1:len(raw_data)])

wonBingos = []
total_score = 0

for i in numbersList:
    for board in boards:
        if board in wonBingos:
            continue
        
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == int(i):
                    board[x][y] = -1
        
        if check_board(board):
            total_score = score(board) * int(i)
            wonBingos.append(board)


print(f"Winning score: {total_score}")



'''
            check = all(item in numbers for item in line)
            if check == True:
                if board in boards:
                    boards.remove(board)
                #return
        for i in range(5):
            for j in range(5):
                column.append(board[j][i])
            check = all(item in numbers for item in column)
            if check == True:
                if board in boards:
                    boards.remove(board)
                #return
            else:
                column = []
    draw_numbers(drawn_numbers[:count], boards)
    if len(boards) == 1:
        winning_number = int(i)
        winning_board = boards[0]
        break
    else:
        winning_board =  []
    count += 1

for line in winning_board:
    for item in line:
        if item not in drawn_numbers[:count + 1]:
            sum_unmarked += int(item)
'''