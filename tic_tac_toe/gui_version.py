import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import check_winner, minimax  # Reuse game logic

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.current_player = "X"  # Human starts first
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        # Create widgets
        self.buttons = []
        self.create_board()
        self.status_label = tk.Label(root, text="Your turn (X)", font=('Arial', 14))
        self.status_label.pack(pady=10)
        self.reset_button = tk.Button(root, text="New Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    frame,
                    text=" ",
                    font=('Arial', 20),
                    width=4,
                    height=2,
                    command=lambda i=i, j=j: self.on_click(i, j)
                )
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, i, j):
        if self.board[i][j] == " " and self.current_player == "X":
            self.board[i][j] = "X"
            self.buttons[i][j].config(text="X")
            if check_winner(self.board, "X"):
                self.status_label.config(text="You win!")
                self.disable_buttons()
            elif all(cell != " " for row in self.board for cell in row):
                self.status_label.config(text="It's a draw!")
            else:
                self.current_player = "O"
                self.status_label.config(text="AI's turn (O)")
                self.root.after(500, self.ai_move)

    def ai_move(self):
        best_score = -float('inf')
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.board[best_move[0]][best_move[1]] = "O"
        self.buttons[best_move[0]][best_move[1]].config(text="O")
        if check_winner(self.board, "O"):
            self.status_label.config(text="AI wins!")
            self.disable_buttons()
        elif all(cell != " " for row in self.board for cell in row):
            self.status_label.config(text="It's a draw!")
        else:
            self.current_player = "X"
            self.status_label.config(text="Your turn (X)")

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text=" ", state=tk.NORMAL)
        self.status_label.config(text="Your turn (X)")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()