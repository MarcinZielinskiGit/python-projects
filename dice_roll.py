import random

result = random.randint(1, 6)
print('Dice roll result: ', result)

while True:
    again = input('Would you like to roll again (y/n): ')
    if again == 'y':
        result = random.randint(1, 6)
        print('Dice roll result: ', result)
    elif again == 'n':
        break
    else:
        print('Incorrect input. Try again.')