# ============================================
#       AKWANYAHUB PYTHON ESSENTIALS
#              TIC-TAC-TOE
# ============================================


def show_title():
    print()
    print("========================================")
    print("             TIC-TAC-TOE")
    print("========================================")
    print("Get 3 of your symbols in a row to win!")
    print()


def show_board(board):
    print()
    print("     |     |")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("_____|_____|_____")
    print("     |     |")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("_____|_____|_____")
    print("     |     |")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("     |     |")
    print()


def show_positions():
    print("Board positions:")
    print()
    print("  1 | 2 | 3")
    print(" ---+---+---")
    print("  4 | 5 | 6")
    print(" ---+---+---")
    print("  7 | 8 | 9")
    print()


def check_winner(board, symbol):

    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for positions in winning_positions:

        first = positions[0]
        second = positions[1]
        third = positions[2]

        if (
            board[first] == symbol
            and board[second] == symbol
            and board[third] == symbol
        ):
            return True

    return False


def board_is_full(board):

    for position in board:
        if position == " ":
            return False

    return True


def get_move(player_name, symbol, board):

    while True:

        print(player_name + "'s turn (" + symbol + ")")

        choice = input("Choose a position from 1 to 9: ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print()
            print("Invalid choice. Please enter a number from 1 to 9.")
            print()
            continue

        position = int(choice) - 1

        if board[position] != " ":
            print()
            print("That position has already been taken.")
            print()
            continue

        return position


def show_scoreboard(players, scores):

    print()
    print("========================================")
    print("               SCOREBOARD")
    print("========================================")

    print(players["X"] + " (X): " + str(scores["X"]))
    print(players["O"] + " (O): " + str(scores["O"]))
    print("Draws: " + str(scores["Draws"]))

    print("========================================")
    print()


def play_round(players):

    board = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " "
    ]

    current_symbol = "X"

    show_positions()

    while True:

        show_board(board)

        current_player = players[current_symbol]

        move = get_move(
            current_player,
            current_symbol,
            board
        )

        board[move] = current_symbol

        if check_winner(board, current_symbol):

            show_board(board)

            print("========================================")
            print("🎉 " + current_player + " wins!")
            print("========================================")

            return current_symbol

        if board_is_full(board):

            show_board(board)

            print("========================================")
            print("It's a draw!")
            print("========================================")

            return "Draws"

        if current_symbol == "X":
            current_symbol = "O"
        else:
            current_symbol = "X"


def main():

    show_title()

    player_one = input("Enter Player 1's name: ")
    player_two = input("Enter Player 2's name: ")

    players = {
        "X": player_one,
        "O": player_two
    }

    scores = {
        "X": 0,
        "O": 0,
        "Draws": 0
    }

    print()
    print(player_one + " will play as X")
    print(player_two + " will play as O")

    while True:

        winner = play_round(players)

        scores[winner] = scores[winner] + 1

        show_scoreboard(players, scores)

        again = input("Play another round? (yes/no): ")

        if again == "yes":
            print()
            print("Starting another round...")
            continue

        elif again == "no":
            break

        else:
            print()
            print("Response not recognised.")
            print("The game will end.")
            break

    print()
    print("========================================")
    print("            FINAL SCOREBOARD")
    print("========================================")

    show_scoreboard(players, scores)

    print("Thanks for playing Tic-Tac-Toe!")
    print()


main()