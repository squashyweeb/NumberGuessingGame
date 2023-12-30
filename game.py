import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        
        self.master.geometry("300x250")
        self.master.resizable(False, False)
        self.master.configure(bg="#e6e6e6")

        self.target_number = random.randrange(1, 10)
        self.used_numbers = []
        self.remaining_guesses = 5

        self.label = tk.Label(master, text="Enter any number: 1-10", font=("Helvetica", 12), bg="#e6e6e6")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.submit_button.pack()

        self.used_numbers_label = tk.Label(master, text="Numbers Used:", font=("Helvetica", 10), bg="#e6e6e6")
        self.used_numbers_label.pack()

        self.used_numbers_display = tk.Label(master, text="", font=("Helvetica", 10), bg="#e6e6e6")
        self.used_numbers_display.pack()

        self.remaining_guesses_label = tk.Label(master, text=f"Remaining Guesses: {self.remaining_guesses}", font=("Helvetica", 10), bg="#e6e6e6")
        self.remaining_guesses_label.pack()

    def check_guess(self):
        if self.remaining_guesses == 0:
            messagebox.showinfo("Game Over", "You've used all your guesses. The correct number was {}".format(self.target_number))
            self.master.destroy()
            return

        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        self.used_numbers.append(guess)

        if guess < self.target_number:
            messagebox.showinfo("Result", "Too low")
        elif guess > self.target_number:
            messagebox.showinfo("Result", "Too high")
        else:
            messagebox.showinfo("Result", f"You guessed it right!! The correct number was {self.target_number}")
            self.master.destroy()

        # Update 
        self.used_numbers_display.config(text=", ".join(map(str, self.used_numbers)))

        # Update guesses
        self.remaining_guesses -= 1
        self.remaining_guesses_label.config(text=f"Remaining Guesses: {self.remaining_guesses}")

        # Clear the entry for the next guess
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
