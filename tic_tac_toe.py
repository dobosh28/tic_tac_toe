def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for i, row in enumerate(board):
        if i > 0:
            print("--+---+--")
        print(" | ".join(row))


def main():
    print("Welcome to Tic Tac Toe!")
    board = initialize_board()
    print_board(board)


if __name__ == "__main__":
    main()


