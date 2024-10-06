import random
import sys

# Initialize the board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Function to display the board
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to check if a player has won
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

# Function to check if the game is a draw
def check_draw():
    return all(space != ' ' for space in board)

# Function to find the best move for the computer (either to win or block)
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
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == player and board[combo[2]] == ' ':
            return combo[2]
        if board[combo[1]] == board[combo[2]] == player and board[combo[0]] == ' ':
            return combo[0]
        if board[combo[0]] == board[combo[2]] == player and board[combo[1]] == ' ':
            return combo[1]
    return None

# Function to execute the computer's move
def computer_move():
    move = find_best_move('O')
    if move is not None:
        board[move] = 'O'
        return
    
    move = find_best_move('X')
    if move is not None:
        board[move] = 'O'
        return
    
    available_moves = [i for i in range(len(board)) if board[i] == ' ']
    if available_moves:
        move = random.choice(available_moves)
        board[move] = 'O'

# Function to reset the board for a new game
def reset_board():
    global board
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Function to play the game
def play_game():
    global board
    while True:
        players = input("Enter number of players (1 or 2): ")

        if players not in ['1', '2', '0']:
            print("Invalid input. Please enter 1, 2 or 0 to quit.")
            continue
        
        if players == "0":
            print("Goodbye!")
            sys.exit()

        current_player = 'X'
        reset_board()
        print_board()

        while True:
            if players == '1' and current_player == 'O':
                print("Computer's turn...")
                computer_move()
                print_board()
            else:
                move = input(f"Player {current_player}, enter your move (1-9): ")

                if move == '0':
                    print("Goodbye!")
                    sys.exit()

                if not move.isdigit() or int(move) not in range(1, 10):
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue

                move = int(move) - 1

                if board[move] != ' ':
                    print("This spot is already taken. Please choose another one.")
                    continue

                board[move] = current_player
                print_board()

            if check_winner(current_player):
                print(f"Player {current_player} wins!")
                break
            if check_draw():
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            sys.exit()

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    print("Press 0 to end the game.")
    play_game()
