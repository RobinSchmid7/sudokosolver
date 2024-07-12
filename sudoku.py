"""
Sudoko Solver with zero imports
Robin Schmid
"""

MAX_NUM_IT = 200 # Max number of iterations before it should stop
INPUT_GAME = False  # True if enter initial game state via terminal input, False to load hardcoded

# Initial game state, gets loaded when INPUT_GAME is set to False
INIT_GAME_STATE = [[0, 6, 2, 3, 4, 0, 7, 5, 0],
             [1, 0, 0, 0, 0, 5, 6, 0, 0],
             [5, 7, 0, 0, 0, 0, 0, 4, 0],
             [0, 0, 0, 0, 9, 4, 8, 0, 0],
             [4, 0, 0, 0, 0, 0, 0, 0, 6],
             [0, 0, 5, 8, 3, 0, 0, 0, 0],
             [0, 3, 0, 0, 0, 0, 0, 9, 1],
             [0, 0, 6, 4, 0, 0, 0, 0, 7],
             [0, 5, 9, 0, 8, 3, 2, 6, 0]]


class Sudoku():
    def __init__(self):
        """Initializes the game with all 0, unkowns"""
        self.board = []
        row = []
        for _ in range(0, 9):
            row.append(0)
        for _ in range(0, 9):
            self.board.append(row)

    def check_finished(self):
        """Checks if the game is solved"""
        cnt = 0
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] == 0:
                    cnt += 1
        if cnt == 0:
            return 1

    def enter_game(self):
        """Enters the initial game state, 0 is unknown"""
        for i in range(0, 9):
            print(f"Enter the row {i+1}/9 and press enter after each number.")
            j = 0
            while j < 9:
                num = int(input())
                if num not in range(0, 10):
                    print("Please enter a valid number!")
                else:
                    print(f"Entered number {num} for position position [{i+1},{j+1}]")
                    self.board[i][j] = num
                    j += 1

    def print_board(self):
        """Prints the board"""
        if self.board == None:
            print("No board loaded")
        else:
            out = self.board

            for i in range(0, 9):
                str_out = ""
                if i % 3 == 0 and i != 0:
                    str_out += "---------------------\n"
                for j in range(0, 9):
                    if j % 3 == 0 and j != 0:
                        str_out += "| "
                    str_out += str(out[i][j]) + " "
                print(str_out)
            print("\n")

    def logic(self, i_, j_):
        """Simple logic to iterate through rows, columns 
        and blocks and adds the only possible number"""
        pos_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        i_block = (i_ // 3) * 3
        j_block = (j_ // 3) * 3

        # Check which numbers are possible in a row
        for i in range(0, 9):
            for p in pos_num:
                if self.board[i][j_] == p:
                    pos_num.remove(p)

        # Check which numbers are possible in a column
        for j in range(0, 9):
            for p in pos_num:
                if self.board[i_][j] == p:
                    pos_num.remove(p)

        # Check which numbers are possible in a block
        for i in range(i_block, i_block + 3):
            for j in range(j_block, j_block + 3):
                for p in pos_num:
                    if self.board[i][j] == p:
                        pos_num.remove(p)

        # If only one number is possible, this must be there
        if len(pos_num) == 1:
            print(f"New number at position [{i_+1},{j_+1}] is {pos_num[0]}")
            self.board[i_][j_] = pos_num[0]
            self.print_board()


if __name__ == '__main__':
    sud = Sudoku()

    if INPUT_GAME:
        sud.enter_game()
        sud.print_board()
    else:
        sud.board = INIT_GAME_STATE

    # Iterate through all options
    for n in range(0, MAX_NUM_IT):
        for i in range(0,9):
            for j in range(0,9):
                if sud.board[i][j] == 0:
                    sud.logic(i, j)

        if sud.check_finished():
            print("Game finished!")
            print(f"Total number of iterations through whole board: {n}")
            exit()
