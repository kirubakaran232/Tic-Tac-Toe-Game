import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Tic Tac Toe")
        self.root.resizable(False, False)
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Player X's Turn", font=("Arial", 16, "bold"), bg="lightblue")
        self.label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=(i // 3) + 1, column=i % 3, sticky="nsew", padx=5, pady=5)
            self.buttons.append(btn)

        self.reset_btn = tk.Button(self.root, text="🔄 Restart", font=("Arial", 12),
                                   command=self.reset_game, bg="orange")
        self.reset_btn.grid(row=4, column=0, columnspan=3, sticky="nsew")

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state="disabled",
                                       disabledforeground="black" if self.current_player == "X" else "blue")

            if self.check_winner():
                self.label.config(text=f"🎉 Player {self.current_player} Wins!")
                self.disable_all_buttons()
                messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!")
            elif "" not in self.board:
                self.label.config(text="🤝 It's a Draw!")
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] != "":
                self.highlight_winner(a, b, c)
                return True
        return False

    def highlight_winner(self, a, b, c):
        self.buttons[a].config(bg="lightgreen")
        self.buttons[b].config(bg="lightgreen")
        self.buttons[c].config(bg="lightgreen")

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.label.config(text="Player X's Turn")
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="SystemButtonFace")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
