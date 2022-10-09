from random import randint

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
    """
    generates ships on random spots on the board
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = shoot_your_shot()
        board[ship_row][ship_column] = "X"

def shoot_your_shot():
    """
    takes input from the player and warns the player if the input is correct or not
    """
    row = input("Enter the row you wish to hit: \n").upper()
    while row not in "12345678":
        print('Where are you aiming at?')
        row = input("Enter the row you wish to hit: \n").upper()
    column = input("Enter the column you wish to hit: \n").upper()
    while column not in "ABCDEFGH":
        print('Where are you aiming at?')
        column = input("Enter the column you wish to hit: \n").upper()
    return int(row) - 1, letters_to_numbers[column]

def ships_hit(board):
    """
    counts the hits 
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    spawn_ships(SHIPS_BOARD)
    turns = 25
    while turns > 0:
        print('Welcome to Battleship!\n')
        print('Guess a row and column \n To start the game! \n')
        print_board(PLAYER_BOARD)
        row, column = shoot_your_shot()
        if PLAYER_BOARD[row][column] == "O":
            print("You hit that one already.")
        elif SHIPS_BOARD[row][column] == "X":
            print("Hit")
            PLAYER_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            PLAYER_BOARD[row][column] = "O"   
            turns -= 1     
        if ships_hit(PLAYER_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("No more turns! Game over!")