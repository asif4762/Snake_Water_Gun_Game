import random
import tkinter as tk
from tkinter import messagebox

# Mapping choices
youDist = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDist = {1: "Snake", -1: "Water", 0: "Gun"}

# Function to play game
def play(choice):
    computer = random.choice([1, -1, 0])
    you = youDist[choice]

    result = ""
    if computer == you:
        result = "It's a Draw!"
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        result = "You Win!"
    else:
        result = "You Lose!"

    # Show result in a message box
    messagebox.showinfo("Result", f"You chose: {choice}\nComputer chose: {reverseDist[computer]}\n{result}")

# Creating UI window
root = tk.Tk()
root.title("Snake-Water-Gun Game")
root.geometry("300x300")

# Adding buttons for choices
tk.Label(root, text="Choose one:", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="Snake", font=("Arial", 12), command=lambda: play("Snake")).pack(pady=5)
tk.Button(root, text="Water", font=("Arial", 12), command=lambda: play("Water")).pack(pady=5)
tk.Button(root, text="Gun", font=("Arial", 12), command=lambda: play("Gun")).pack(pady=5)

# Run the GUI
root.mainloop()
