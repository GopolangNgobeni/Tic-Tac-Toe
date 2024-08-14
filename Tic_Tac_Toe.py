import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(player):
    winning_combinations = [
        (0, 1, 2),  # Row 1
        (3, 4, 5),  # Row 2
        (6, 7, 8),  # Row 3
        (0, 3, 6),  # Column 1
        (1, 4, 7),  # Column 2
        (2, 5, 8),  # Column 3
        (0, 4, 8),  # Diagonal 1
        (2, 4, 6)   # Diagonal 2
    ]
    
    # Checking if any winning combination is met
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    
    return False

def check_draw():
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

# Function to get a winning or blocking move
def find_best_move(player):
    winning_combinations = [
        (0, 1, 2),  # Row 1
        (3, 4, 5),  # Row 2
        (6, 7, 8),  # Row 3
        (0, 3, 6),  # Column 1
        (1, 4, 7),  # Column 2
        (2, 5, 8),  # Column 3
        (0, 4, 8),  # Diagonal 1
        (2, 4, 6)   # Diagonal 2
    ]
    
    # Checking if a move can win or block the opponent
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == player and board[combo[2]] == ' ':
            return combo[2]
        if board[combo[1]] == board[combo[2]] == player and board[combo[0]] == ' ':
            return combo[0]
        if board[combo[0]] == board[combo[2]] == player and board[combo[1]] == ' ':
            return combo[1]
    
    return None

def computer_move():
    # Checking if the computer can win
    move = find_best_move('O')
    if move is not None:
        board[move] = 'O'
        return
    
    # Checking if the player is about to win and block it
    move = find_best_move('X')
    if move is not None:
        board[move] = 'O'
        return
    
    # If no immediate win or block, choose randomly from available spots
    available_moves = []
    for i in range(len(board)):
        if board[i] == ' ':
            available_moves.append(i)
    
    if available_moves:
        move = random.choice(available_moves)
        board[move] = 'O'

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    players = input("Enter number of players (1 or 2): ")

    current_player = 'X'
    
    while True:
        print_board()
        
        if players == '1' and current_player == 'O':
            print("Computer's turn...")
            computer_move()
        else:
            move = input(f"Player {current_player}, enter your move (1-9): ")
            
            if not move.isdigit() or int(move) < 1 or int(move) > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            
            move = int(move) - 1
            
            if board[move] != ' ':
                print("This spot is already taken. Please choose another one.")
                continue
            
            board[move] = current_player
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ == "__main__":
    play_game()
