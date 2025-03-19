import random
import tkinter as tk
from tkinter import messagebox, PhotoImage


def setup_window():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")
    root.configure(bg="#2C3E50")
    return root


def setup_ui(root, game):
    # Initialize game variables and UI
    game.label = tk.Label(root, text="Rock, paper, scissors, shoot!", font=("Helvetica", 16, "bold"), fg="white", bg="#2C3E50")
    game.label.pack(pady=10)

    game.timer_label = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="#2C3E50")
    game.timer_label.pack()

    game.choices = ["rock", "paper", "scissors"]
    game.images = {
        "rock": PhotoImage(file="Images/rock.png").subsample(5, 5),
        "paper": PhotoImage(file="Images/paper.png").subsample(5, 5),
        "scissors": PhotoImage(file="Images/scissors.png").subsample(5, 5)
    }

    game.button_frame = tk.Frame(root, bg="#2C3E50")
    game.button_frame.pack(pady=10)

    game.buttons = []
    for choice in game.choices:
        btn = tk.Button(game.button_frame, image=game.images[choice], command=lambda c=choice: game.play(c),
                        bg="#ECF0F1", activebackground="#BDC3C7", borderwidth=2, relief="flat")
        btn.pack(side=tk.LEFT, padx=10)
        game.buttons.append(btn)

    game.result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), fg="white", bg="#2C3E50")
    game.result_label.pack(pady=10)

    game.play_again_btn = tk.Button(root, text="Play Again", font=("Helvetica", 12, "bold"), command=game.reset_game,
                                    bg="#3498DB", fg="white", activebackground="#2980B9", borderwidth=2, relief="flat", padx=10, pady=5)
    game.play_again_btn.pack(pady=5)

    game.exit_btn = tk.Button(root, text="Exit", font=("Helvetica", 12, "bold"), command=root.quit,
                              bg="#E74C3C", fg="white", activebackground="#C0392B", borderwidth=2, relief="flat", padx=10, pady=5)
    game.exit_btn.pack(pady=5)

# Game logic
class RockPaperScissorsGame:

    def __init__(self, root):
        self.user_wins = 0
        self.computer_wins = 0
        self.root = root
        self.timer = None
        self.time_left = 5
        setup_ui(root, self)
        self.user_label = tk.Label(root, text=f"User Wins: {self.user_wins}", font=("Helvetica", 10), fg="white", bg="#2C3E50")
        self.user_label.pack(anchor="e", padx=10, pady=5)
        self.computer_label = tk.Label(root, text=f"Computer Wins: {self.computer_wins}", font=("Helvetica", 10), fg="white", bg="#2C3E50")
        self.computer_label.pack(anchor="e", padx=10, pady=5)
        self.ask_to_play()

    def ask_to_play(self):
        answer = messagebox.askyesno("Rock, Paper, Scissors", "Are you ready to play?")
        if answer:
            self.start_timer()
        else:
            self.root.destroy()

    def start_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer = self.root.after(1000, self.start_timer)
        else:
            self.disable_buttons()
            self.result_label.config(text="Time's up! You didn't make a choice.")

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def enable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.NORMAL)

    def play(self, user_choice):
        if self.timer:
            self.root.after_cancel(self.timer)  # Stop the timer when a choice is made
            self.timer = None  # Reset timer variable
        
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        self.label.config(text=f"Computer chose: {computer_choice}")
        self.result_label.config(text=result)

        self.disable_buttons()

    def determine_winner(self, user, computer):
     if user == computer:
        return "It's a tie!"
     elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        self.user_wins += 1   #Adds to the scoreboard
        self.user_label.config(text=f"User Wins: {self.user_wins}")
        return "You win!"
     else:
        self.computer_wins += 1   #Adds to the scoreboard
        self.computer_label.config(text=f"Computer Wins: {self.computer_wins}")
        return "Computer wins!"


    def reset_game(self):
        self.label.config(text="Rock, paper, scissors, shoot!")
        self.result_label.config(text="")
        self.time_left = 5
        self.enable_buttons()
        self.ask_to_play()

if __name__ == "__main__":
    root = setup_window()
    game = RockPaperScissorsGame(root)
    root.mainloop()

