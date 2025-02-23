# tic_tac_toe.py
import sys

def print_board(board):
    """Prints the current game board with borders."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    """Checks if the specified player has won."""
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Columns
            return True
    
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == player or
        board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
    return False

def is_board_full(board):
    """Checks if the board is completely filled."""
    return all(cell != " " for row in board for cell in row)

def get_player_move(board):
    """Handles player input with comprehensive validation."""
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Validate input range
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Error: Input must be between 0-2. Try again.")
                continue
                
            # Check cell availability
            if board[row][col] != " ":
                print("That cell is already occupied! Try again.")
                continue
                
            return (row, col)
            
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0-2.")

def minimax(board, depth, is_maximizing):
    """Implements the Minimax algorithm with depth consideration."""
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def ai_move(board):
    """Executes the AI's move using Minimax optimization."""
    best_score = -float('inf')
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    if best_move != (-1, -1):
        board[best_move[0]][best_move[1]] = "O"
    else:
        # Fallback if no valid moves found (should never occur)
        print("AI error: No valid moves available!")
        sys.exit(1)

def play_game():
    """Manages the game flow and state."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Human starts first
    
    print("\nWelcome to Tic-Tac-Toe against AI!")
    print("You're X. Enter row and column numbers (0-2).\n")
    
    while True:
        print_board(board)
        
        if current_player == "X":
            print("\nYour turn:")
            row, col = get_player_move(board)
            board[row][col] = "X"
        else:
            print("\nAI's turn...")
            ai_move(board)

        # Check game status
        if check_winner(board, current_player):
            print_board(board)
            print(f"\n{'You' if current_player == 'X' else 'AI'} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break
            
        current_player = "O" if current_player == "X" else "X"

def main():
    """Main entry point for the game."""
    while True:
        play_game()
        restart = input("\nPlay again? (y/n): ").lower()
        if restart != 'y':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()