# Constants for the game settings 
BOARD_SIZE = 3
EMPTY_CELL = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def initialize_board():
    # Initialize a game board of the size BOARD_SIZE x BOARD_SIZE with all empty cells.
    return [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    # Print the current state of the board.
    # This includes the board itself and horizontal separators between rows.
    for i, row in enumerate(board):
        if i > 0:
            print("---+---+---")
        print(" {} | {} | {} ".format(row[0], row[1], row[2]))

def is_line_win(line):
    # Check if a singel line (row, column, or diagonal) is a winning line.
    # A winning line contains the same player's mark (X or O) in all positions and is not empty.
    return line[0] != EMPTY_CELL and line[0] == line[1] == line[2]

def is_game_over(board):
    # Check if the game is over. This occurs if there's a winning row, column or diagonal.
    for i in range(BOARD_SIZE):
        # Check each row and column
        if is_line_win(board[i]) or is_line_win([board[j][i] for j in range(BOARD_SIZE)]):
            return True
    # Check the two diagonals 
    return is_line_win([board[i][i] for i in range(BOARD_SIZE)]) or \
           is_line_win([board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)])

def is_board_full(board):
    # Check if the board is full (i.e., no empty cells left).
    return all(cell != EMPTY_CELL for row in board for cell in row)

def get_player_move(player, player_name):
    # Prompt the current player to enter their move (row and column).
    # Validate the input to ensure it is an iteger within the board's bounds.
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
    # Check if the move is valid: the chosen cell must be empty.
    if board[row][col] != EMPTY_CELL:
        print("This space is already occupied")
        return False
    return True

def main():
    # The main function to run the Tic Tac Toe game.
    print("Welcome to Tic Tac Toe!")

    # Get player names and start the game loop.
    player1_name = input("Enter name for player 1 (X): ").strip()
    player2_name = input("Enter name for player 2 (O): ").strip()

    while True:
        # Initialize the board and start the round.
        board = initialize_board()
        print_board(board)
        current_player, current_player_name = PLAYER_X, player1_name

        # Game round loop
        while True:
            row, col = get_player_move(current_player, current_player_name)
            if is_valid_move(board, row, col):
                board[row][col] = current_player
                print_board(board)
                if is_game_over(board):
                    print(f"{current_player_name} wins!")
                    break
                if is_board_full(board):
                    print("It's a tie!")
                    break
                # Switch players
                current_player, current_player_name = (PLAYER_O, player2_name) if current_player == PLAYER_X else (PLAYER_X, player1_name)
            else:
                print("Invalid move! Try again.")

        # Prompt for replay
        if input("Play again? (y/n): ").lower() != 'y':
            break

    # End of the game message
    print ("Thanks for playing!")

# Standard boilerplate to call the main() function.
if __name__ == "__main__":
    main()
