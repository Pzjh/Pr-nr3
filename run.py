SHIPS_BOARD = [[" "] * 8 for x in range(8)]

PLAYER_BOARD = [[" "] * 8 for i in range(8)]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

def print_board(board):
    """
    print the board to the player
    """
    print("  A B C D E F G H")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def spawn_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = shoot_your_shot()
        board[ship_row][ship_column] = "X"

def shoot_your_shot():
    row = input("Enter the row you wish to hit: ").upper()
    while row not in "12345678":
        print('Where are you aiming at?')
        row = input("Enter the row you wish to hit: ").upper()
    column = input("Enter the column you wish to hit: ").upper()
    while column not in "ABCDEFGH":
        print('Where are you aiming at?')
        column = input("Enter the column you wish to hit: ").upper()
    return int(row) - 1, letters_to_numbers[column]
