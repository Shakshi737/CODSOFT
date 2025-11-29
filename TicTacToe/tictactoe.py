import math

# Constants for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    """
    Prints the current state of the board in a user-friendly format.
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """
    Checks if the given player has won the game.
    Returns True if the player has won, False otherwise.
    """
    # Winning combinations (indices)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    """
    Checks if the board is full (no empty spaces).
    """
    return EMPTY not in board

def get_available_moves(board):
    """
    Returns a list of indices of available (empty) spots.
    """
    return [i for i, x in enumerate(board) if x == EMPTY]

def minimax(board, depth, is_maximizing):
    """
    The Minimax algorithm.
    Recursively evaluates all possible moves to find the best score.
    
    Scores:
    AI wins: +1
    Human wins: -1
    Draw: 0
    """
    
    # Base cases: check for terminal states
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY # Undo move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY # Undo move
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    """
    Determines the best move for the AI using Minimax.
    """
    best_score = -math.inf
    best_move = None
    
    # If it's the very first move, take the center or a corner to save computation time
    # (Optional optimization, but Minimax on 3x3 is fast enough)
    
    print("AI is thinking...")
    
    for move in get_available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY # Undo move
        
        if score > best_score:
            best_score = score
            best_move = move
            
    return best_move

def human_move(board):
    """
    Prompts the human player for their move.
    """
    while True:
        try:
            move = input("Enter your move (1-9): ")
            move = int(move) - 1 # Convert 1-9 to 0-8 index
            
            if 0 <= move <= 8:
                if board[move] == EMPTY:
                    return move
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main game loop.
    """
    print("=======================================")
    print("       UNBEATABLE TIC-TAC-TOE AI       ")
    print("=======================================")
    print("You are X. The AI is O.")
    print("Positions are numbered 1-9 starting from top-left.")
    
    board = [EMPTY] * 9
    
    # Ask who goes first
    while True:
        choice = input("Do you want to go first? (y/n): ").lower()
        if choice in ['y', 'n']:
            break
        print("Please enter 'y' or 'n'.")
    
    human_turn = (choice == 'y')
    
    while True:
        print_board(board)
        
        if check_winner(board, AI):
            print("AI wins! Better luck next time.")
            break
        if check_winner(board, HUMAN):
            print("You win! (Wait, that's impossible...)")
            break
        if is_board_full(board):
            print("It's a draw! Good game.")
            break
        
        if human_turn:
            move = human_move(board)
            board[move] = HUMAN
        else:
            move = ai_move(board)
            board[move] = AI
            
        human_turn = not human_turn # Switch turns

if __name__ == "__main__":
    main()
