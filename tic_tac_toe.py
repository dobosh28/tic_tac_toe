BOARD_SIZE = 3
EMPTY_CELL = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def initialize_board():
    return [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    for i, row in enumerate(board):
        if i > 0:
            print("---+---+---")
        print(" {} | {} | {} ".format(row[0], row[1], row[2]))

def is_line_win(line):
    return line[0] != EMPTY_CELL and line[0] == line[1] == line[2]

def is_game_over(board):
    for i in range(BOARD_SIZE):
        if is_line_win(board[i]) or is_line_win([board[j][i] for j in range(BOARD_SIZE)]):
            return True
    return is_line_win([board[i][i] for i in range(BOARD_SIZE)]) or \
           is_line_win([board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)])

def get_player_move(player, player_name):
    while True:
        try:
            print(f"{player_name}'s turn ({player}).")
            row = int(input("Enter row (0-2): ").strip())
            col = int(input("Enter column (0-2): ").strip())
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                return row, col
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Please enter a valid integer.")

def is_valid_move(board, row, col):
    if board[row][col] != EMPTY_CELL:
        print("This space is already occupied")
        return False
    return True

def main():
    print("Welcome to Tic Tac Toe!")

    player1_name = input("Enter name for player 1 (X): ").strip()
    player2_name = input("Enter name for player 2 (O): ").strip()

    while True:
        board = initialize_board()
        print_board(board)
        current_player, current_player_name = PLAYER_X, player1_name

        while True:
            row, col = get_player_move(current_player, current_player_name)
            if is_valid_move(board, row, col):
                board[row][col] = current_player
                print_board(board)
                if is_game_over(board):
                    print(f"{current_player_name} wins!")
                    break
                if all(cell != EMPTY_CELL for row in board for cell in row):
                    print("It's a tie!")
                    break
                current_player, current_player_name = (PLAYER_O, player2_name) if current_player == PLAYER_X else (PLAYER_X, player1_name)
            else:
                print("Invalid move! Try again.")

        if input("Play again? (y/n): ").lower() != 'y':
            break

    print ("Thanks for playing!")

if __name__ == "__main__":
    main()
