import random

def get_max_score():
    max_score = input('What will be winning score? (1-99) ')
    try:
        max_score = int(max_score)
    except Exception:
        print(max_score, 'is not number between 1-99. Try again.')
        get_max_score()
    if not 1 <= max_score <= 99:
        print(max_score, 'is not number between 1-99. Try again.')
        get_max_score()
    return max_score

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def result(computer_choice, human_choice):
    global computer_score
    global human_score
    if computer_choice == human_choice:
        print('Tie!')
    elif computer_choice == 'rock' and human_choice == 'paper':
        human_score += 1
        print('Computer choice was ROCK. You won this one!')
    elif computer_choice == 'rock' and human_choice == 'scissors':
        computer_score += 1
        print('Computer choice was ROCK. You lost this one!')
    elif computer_choice == 'paper' and human_choice == 'rock':
        computer_score += 1
        print('Computer choice was PAPER. You lost this one!')
    elif computer_choice == 'paper' and human_choice == 'scissors':
        human_score += 1
        print('Computer choice was PAPER. You won this one!')
    elif computer_choice == 'scissors' and human_choice == 'paper':
        computer_score += 1
        print('Computer choice was SCISSORS. You lost this one!')
    elif computer_choice == 'scissors' and human_choice == 'rock':
        human_score += 1
        print('Computer choice was SCISSORS. You won this one!')

def main():
    global computer_score
    global human_score
    max_score = get_max_score()
    computer_score = 0
    human_score = 0
    while computer_score < max_score and human_score < max_score:
        computer_choice = get_computer_choice()
        # print(computer_choice)
        human_choice = input('What do you choose? (rock/paper/scissors) ')
        if human_choice != 'rock' and human_choice != 'paper' and human_choice != 'scissors':
            print('Incorrect input. Try again.')
        
        result(computer_choice, human_choice)
        print('Computer: ', computer_score, 'points.')
        print('You: ', human_score,'points.')
    
    if computer_score > human_score:
        print('You lost!', human_score, 'to', computer_score, 'points.')
    elif computer_score < human_score:
        print('You won!', human_score, 'to', computer_score, 'points. Congratulations!')

main()