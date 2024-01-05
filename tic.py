import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe Game")

        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

        # Create buttons for the 3x3 grid
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text='', font=('Arial', 24), width=6, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        # Reset button
        self.reset_button = tk.Button(master, text="Reset", font=('Arial', 12), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        if not self.board[row][col]:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True  # Check horizontal
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True  # Check vertical

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True  # Check diagonal (top-left to bottom-right)
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True  # Check diagonal (top-right to bottom-left)

        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False  # There are still empty spaces

        return True  # All spaces are filled, and there is no winner

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe_app = TicTacToeApp(root)
    root.mainloop()
