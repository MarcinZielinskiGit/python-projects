from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Rock Paper Scissors')


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def get_result(human_choice, computer_choice):
    global human_score
    global computer_score
    if human_choice == computer_choice:
        lbl_info['text'] = 'Tie!'
    elif human_choice == 'rock' and computer_choice == 'paper':
        lbl_info['text'] = 'You lost this one.'
        computer_score += 1
    elif human_choice == 'rock' and computer_choice == 'scissors':
        lbl_info['text'] = 'You won this one.'
        human_score += 1
    elif human_choice == 'paper' and computer_choice == 'rock':
        lbl_info['text'] = 'You won this one.'
        human_score += 1
    elif human_choice == 'paper' and computer_choice == 'scissors':
        lbl_info['text'] = 'You lost this one.'
        computer_score += 1
    elif human_choice == 'scissors' and computer_choice == 'rock':
        lbl_info['text'] = 'You lost this one.'
        computer_score += 1
    elif human_choice == 'scissors' and computer_choice == 'paper':
        lbl_info['text'] = 'You won this one.'
        human_score += 1

    return lbl_scores['text'] = f'HUMAN {human_score} : {computer_score} COMPUTER'


def human_choosed(choice):
    human_choice = choice
    computer_choice = get_computer_choice()
    lbl_human_choice['text'] = f'Human choice: \n {human_choice}'
    lbl_computer_choice['text'] = f'Computer choice: \n {computer_choice}'
    get_result(human_choice, computer_choice)


global human_score
global computer_score
human_score = 0
computer_score = 0
global human_choice
global computer_choice
human_choice = None
computer_choice = None

# Displays scores
lbl_scores_top = Label(root, text='SCORES')
lbl_scores_top.grid(row=0, column=1)
lbl_scores = Label(
    root, text=f'HUMAN {human_score} : {computer_score} COMPUTER')
lbl_scores.grid(row=1, column=0, columnspan=3, pady=5)

# Buttons to make a choice
rock_button = Button(root, text='Rock', width=10,
                     command=lambda: human_choosed('rock'))
rock_button.grid(row=2, column=0)
paper_button = Button(root, text='Paper', width=10,
                      command=lambda: human_choosed('paper'))
paper_button.grid(row=2, column=1)
scissors_button = Button(root, text='Scissors', width=10,
                         command=lambda: human_choosed('scissors'))
scissors_button.grid(row=2, column=2)

# Dispalys human and computer choices and result of the round
lbl_human_choice = Label(root, text=f'Human choice: \n {human_choice}')
lbl_human_choice.grid(row=4, column=0, rowspan=2)
lbl_computer_choice = Label(
    root, text=f'Computer choice: \n {computer_choice}')
lbl_computer_choice.grid(row=4, column=2, rowspan=2)
lbl_info = Label(root, text='Make a choice to start the game.')
lbl_info.grid(row=3, column=0, columnspan=3, pady=5)


root.mainloop()
