import random
 
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board
 
def add_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4
 
def print_board(board):
    for row in board:
        print('\t'.join(str(cell) if cell != 0 else '-' for cell in row))
        print()
 
def slide_left(row):
    merged = [False] * 4
    new_row = []
    for i in range(4):
        if row[i] != 0:
            if new_row and new_row[-1] == row[i] and not merged[i - 1]:
                new_row[-1] *= 2
                merged[i - 1] = True
            else:
                new_row.append(row[i])
    new_row.extend([0] * (4 - len(new_row)))
    return new_row
 
def move_left(board):
    new_board = []
    for row in board:
        new_row = slide_left(row)
        new_board.append(new_row)
    return new_board
 
 
def rotate_board(board):
    return [list(row) for row in zip(*board[::-1])]
 
def perform_move(board, direction):
    if direction == 'up':
        board = rotate_board(board)
        board = move_left(board)
        board = rotate_board(board)
    elif direction == 'down':
        board = rotate_board(board)
        board = rotate_board(board)
        board = move_left(board)
        board = rotate_board(board)
        board = rotate_board(board)
    elif direction == 'left':
        board = move_left(board)
    elif direction == 'right':
        board = rotate_board(board)
        board = rotate_board(board)
        board = rotate_board(board)
        board = move_left(board)
        board = rotate_board(board)
    return board
 
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i > 0 and board[i][j] == board[i - 1][j]:
                return False
            if j > 0 and board[i][j] == board[i][j - 1]:
                return False
    return True
 
# Main game loop
def play_game():
    board = initialize_board()
    print_board(board)
    while not is_game_over(board):
        direction = input("Enter move direction (up/down/left/right): ").strip().lower()
        if direction in ['up', 'down', 'left', 'right']:
            board = perform_move(board, direction)
            add_random_tile(board)
            print_board(board)
        else:
            print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")
    print("Game over!")
 
if __name__ == '__main__':
    play_game()
