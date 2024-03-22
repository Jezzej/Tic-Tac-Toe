from tkinter import *
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

class TicTacToe_Board(Tk):
    def __init__(self):
        super().__init__()
        self.title("TIC-TAC-TOE GAME")
        self.current_player = Player(label="X", color="blue")
        self.other_player = Player(label="O", color="red")
        self._cells = {}
        self.game_over = False
        self.moves = [[None]*3 for _ in range(3)]  # To keep track of moves
        self.create_grid()
        self.board_display()
        
    def board_display(self):
        display_frame = Frame(master=self)
        display_frame.pack(fill=X)
        self.display = Label(
            master=display_frame, text=f"Current Player: {self.current_player.label}",
            font="helvetica 20 bold")
        self.display.pack()

    def create_grid(self):
        grid_frame = Frame(master=self, bg="white")
        grid_frame.pack()
        colors = ["grey", "light blue"]
        colors_index = 0
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = Button(master=grid_frame, text="", font="arial 36 bold",
                                fg="black", width=3, height=1, highlightbackground="grey",
                                bg=colors[colors_index % len(colors)])
                button.config(command=lambda b=button: self.on_button_click(b))
                self._cells[button] = (row, col)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                colors_index += 1
    
    def on_button_click(self, button):
        if not self.game_over:
            row, col = self._cells[button]
            if not self.moves[row][col]:
                self.moves[row][col] = self.current_player.label
                button.config(text=self.current_player.label)
                if self.check_winner(row, col):
                    self.display.config(text=f"Player {self.current_player.label} wins!")
                    self.game_over = True
                elif self.check_draw():
                    self.display.config(text="It's a draw!")
                    self.game_over = True
                else:
                    self.current_player, self.other_player = self.other_player, self.current_player
                    self.display.config(text=f"Current Player: {self.current_player.label}")

    def check_winner(self, row, col):
        label = self.moves[row][col]
        # Check row
        if all(self.moves[row][c] == label for c in range(3)):
            return True
        # Check column
        if all(self.moves[r][col] == label for r in range(3)):
            return True
        # Check diagonal
        if row == col and all(self.moves[i][i] == label for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(self.moves[i][2-i] == label for i in range(3)):
            return True
        return False
    
    def check_draw(self):
        return all(all(cell for cell in row) for row in self.moves)

def main():
    board = TicTacToe_Board()
    board.mainloop()

if __name__ == "__main__":
    main()
