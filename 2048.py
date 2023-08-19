import random

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.add_random_tile()
        self.add_random_tile()
        
    def initialize_board(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.add_random_tile()
        self.add_random_tile()
    
    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4
    
    def print_board(self):
        for row in self.board:
            print('\t'.join(str(cell) if cell != 0 else '-' for cell in row))
            print()
    
    def slide_left(self, row):
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
    
    def move_left(self):
        new_board = []
        for row in self.board:
            new_row = self.slide_left(row)
            new_board.append(new_row)
        self.board = new_board
    
    def rotate_board(self):
        self.board = [list(row) for row in zip(*self.board[::-1])]
    
    def perform_move(self, direction):
        if direction == 'up':
            self.rotate_board()
            self.move_left()
            self.rotate_board()
        elif direction == 'down':
            self.rotate_board()
            self.rotate_board()
            self.move_left()
            self.rotate_board()
            self.rotate_board()
        elif direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.rotate_board()
            self.rotate_board()
            self.rotate_board()
            self.move_left()
            self.rotate_board()
    
    def is_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False
                if i > 0 and self.board[i][j] == self.board[i - 1][j]:
                    return False
                if j > 0 and self.board[i][j] == self.board[i][j - 1]:
                    return False
        return True
    
    def play_game(self):
        self.initialize_board()
        self.print_board()
        while not self.is_game_over():
            direction = input("Enter move direction (up/down/left/right): ").strip().lower()
            if direction in ['up', 'down', 'left', 'right']:
                self.perform_move(direction)
                self.add_random_tile()
                self.print_board()
            else:
                print("Invalid direction. Please enter 'up', 'down', 'left', or 'right'.")
        print("Game over!")

if __name__ == '__main__':
    game = Game2048()
    game.play_game()
