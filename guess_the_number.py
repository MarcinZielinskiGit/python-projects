import random

computer = random.randint(1, 10)\

print(computer)

print('Computer picked random number form 1 to 10. Guess the number: ')
human = int(input())

while human!= computer:
    if human > computer:
        print('Yours number is too big. Guess again: ')
        human = int(input())
    else:
        print('Yours number is too small. Guess again: ')
        human = int(input())

print('Congratulation! You have guessed the number!')