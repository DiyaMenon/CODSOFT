from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title('Rock, Paper, Scissors')
root.geometry("500x600")
root.config(bg="beige")

# Defining the images for rock, paper, scissors
rock = PhotoImage(file="rock.png")
paper = PhotoImage(file="paper.png")
scissors = PhotoImage(file="scissors.png")

# Add images to a list
image_list = [rock, paper, scissors]

# Pick random number between 0 and 2
ran_no = randint(0, 2)

# Image when program starts
image_label = Label(root, image=image_list[ran_no], bd=0)
image_label.pack(pady=20)

# Label to display win/lose messages
win_lose_label = Label(root, text="", font=("Arial", 14), bg="beige")
win_lose_label.pack(pady=10)

# Function for spin
def spin():
    pick_number = randint(0, 2)
    image_label.config(image=image_list[pick_number])
    
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2
    
    # Determine if we won or lost
    if user_choice_value == 0: # Rock
        if pick_number == 0:
            win_lose_label.config(text="It's A Tie! Spin Again...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Paper Covers Rock! You Lose...")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Rock Smashes Scissors! You Win!!!")
    
    # If User Picks Paper
    if user_choice_value == 1: # Paper
        if pick_number == 1:
            win_lose_label.config(text="It's A Tie! Spin Again...")
        elif pick_number == 0: # Rock
            win_lose_label.config(text="Paper Covers Rock! You Win!!!")
        elif pick_number == 2: # Scissors
            win_lose_label.config(text="Scissors Cuts Paper! You Lose...")
    
    # If User Picks Scissors
    if user_choice_value == 2: # Scissors
        if pick_number == 2:
            win_lose_label.config(text="It's A Tie! Spin Again...")
        elif pick_number == 0: # Rock
            win_lose_label.config(text="Rock Smashes Scissors! You Lose...")
        elif pick_number == 1: # Paper
            win_lose_label.config(text="Scissors Cuts Paper! You Win!!!")

# Making a choice
user_choice = ttk.Combobox(root, values=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

# Button to spin and play again
spin_btn = Button(root, text="Spin!", command=spin)
spin_btn.pack(pady=10)

root.mainloop()
