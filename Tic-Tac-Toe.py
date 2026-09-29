import random


def display_board(board):
    print()
    print("-------------")

    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("-------------")


def check_winner(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if (board[0][0] == player and
        board[1][1] == player and
        board[2][2] == player):
        return True

    if (board[0][2] == player and
        board[1][1] == player and
        board[2][0] == player):
        return True

    return False


def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    return True


def ai_move(board):

    empty_positions = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_positions.append((row, col))

    row, col = random.choice(empty_positions)

    board[row][col] = "X"


def tic_tac_toe():

    board = [[" " for _ in range(3)] for _ in range(3)]

    print("You are O")
    print("AI is X")

    while True:

        print("\nAI's turn...")

        ai_move(board)

        display_board(board)

        if check_winner(board, "X"):
            print("AI wins!")
            return

        if board_full(board):
            print("It's a draw!")
            return

        print("\nYour turn (O)")

        while True:
            try:
                position = int(input("Enter position (1-9): "))

                if position < 1 or position > 9:
                    print("Enter a number between 1 and 9.")
                    continue

                row = (position - 1) // 3
                col = (position - 1) % 3

                if board[row][col] != " ":
                    print("Position already occupied. Try again.")
                    continue

                board[row][col] = "O"
                break

            except ValueError:
                print("Please enter a valid number.")

        display_board(board)

        if check_winner(board, "O"):
            print("You win!")
            return

        if board_full(board):
            print("It's a draw!")
            return


tic_tac_toe()
