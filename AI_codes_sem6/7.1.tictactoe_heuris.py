import random

# Board representation
board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_full():
    return " " not in board

def player_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Invalid move. Try again.")

# Heuristic AI
def ai_move():

    # 1. Win if possible
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "

    # 2. Block player win
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "

    # 3. Take center
    if board[4] == " ":
        board[4] = "O"
        return

    # 4. Take corners
    corners = [0,2,6,8]
    random.shuffle(corners)
    for i in corners:
        if board[i] == " ":
            board[i] = "O"
            return

    # 5. Take sides
    sides = [1,3,5,7]
    random.shuffle(sides)
    for i in sides:
        if board[i] == " ":
            board[i] = "O"
            return

# Game loop
print("Tic Tac Toe")
print("You are X | AI is O")

while True:
    
    print_board()
    player_move()

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_full():
        print_board()
        print("Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if is_full():
        print_board()
        print("Draw!")
        break