'''
V1.2 changes:
- added 'Start new game button'
- when starting new game you have to choose what would be winning result
- additional label showing what's the winning result
- messages when game finished- you can coose to play another game or finish
'''

from tkinter import *
from tkinter import messagebox
import random

# Defines global variables used to track points, choices and winning result
global human_score, computer_score
human_score = 0
computer_score = 0
global human_choice, computer_choice
human_choice = None
computer_choice = None
global winning_result
winning_result = 0


def new_game():
    global human_score, computer_score
    human_score = 0
    computer_score = 0
    lbl_scores['text'] = f'HUMAN {human_score} : {computer_score} COMPUTER'
    popup = Toplevel()
    popup.title('Choose number of attempts')
    label_popup = Label(
        popup, text='What would you like to be winning score? (1-99)')
    label_popup.pack()
    entry_popup = Entry(popup, width=10)
    entry_popup.pack()
    accept_button = Button(popup, text='Accept',
                           command=lambda: check_max_score(entry_popup.get()))
    accept_button.pack()

    def check_max_score(max_score):
        global winning_result
        try:
            max_score = int(max_score)
        except Exception:
            return messagebox.showwarning('Incorrect input', 'Please enter correct number between 1 and 99.')
        if 1 <= max_score <= 99:
            popup.destroy()
            winning_result = max_score
            lbl_winning_result['text'] = f'Whoever gets {winning_result} points first wins.'
            lbl_info['text'] = '*** Now pick you choice: Rock, Paper or Scissors ***'
            return winning_result
        else:
            return messagebox.showwarning('Incorrect input', 'Please enter correct number between 1 and 99.')


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def get_result(human_choice, computer_choice):
    global human_score, computer_score
    global winning_result
    # Checks who won the round and adding points
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
    # Updates points in GUI
    lbl_scores['text'] = f'HUMAN {human_score} : {computer_score} COMPUTER'
    # Checks if winning result reached yet
    if human_score == winning_result:
        winning_result = 0
        if messagebox.askyesno('Congratulations!', 'Congratulations! You won! :) \n Do you want to play again?') == 0:
            lbl_winning_result['text'] = 'Congratulations! You won!!!'
            lbl_info['text'] = 'Press "Start new game" to play again'
        else:
            return new_game()
    elif computer_score == winning_result:
        winning_result = 0
        if messagebox.askyesno('You lost!', 'You lost with computer :( \n Do you want revange?') == 0:
            lbl_winning_result['text'] = 'You lost :( Try again.'
            lbl_info['text'] = 'Press "Start new game" to play again'
        else:
            return new_game()


def human_choosed(choice):
    global winning_result
    if winning_result == 0:
        return messagebox.showwarning('Start new game', 'Click "Start new game" to choose winning result fisrt.')
    else:
        human_choice = choice
        computer_choice = get_computer_choice()
        lbl_human_choice['text'] = f'Human choice: \n {human_choice}'
        lbl_computer_choice['text'] = f'Computer choice: \n {computer_choice}'
        get_result(human_choice, computer_choice)


# Main window
root = Tk()
root.title('Rock Paper Scissors')

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

# Displays winning result and 'Start new game' button
lbl_winning_result = Label(
    root, text='*** Click "Start new game" below to start. ***')
lbl_winning_result.grid(row=3, column=0, columnspan=3)
start_button = Button(root, text='Start new game', command=new_game)
start_button.grid(row=4, column=1, pady=5)

# Dispalys human and computer choices and result of the round
lbl_info = Label(root)
lbl_info.grid(row=5, column=0, columnspan=3, pady=5)
lbl_human_choice = Label(root, text=f'Human choice: \n {human_choice}')
lbl_human_choice.grid(row=6, column=0, rowspan=2)
lbl_computer_choice = Label(
    root, text=f'Computer choice: \n {computer_choice}')
lbl_computer_choice.grid(row=6, column=2, rowspan=2)


root.mainloop()
