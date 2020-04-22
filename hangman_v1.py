import random


def checkletter(letter):
    if len(letter) != 1:
        print('Incorrect input. Please enter only one letter.')
    else:
        for i in range(len(myword)):
            if letter == myword[i]:
                blankword[i] = letter

    print(*blankword, sep=' ')


words = open('words.txt', 'r').read().splitlines()

myword = []

for i in random.choice(words):
    myword.append(i)

print(myword)

blankword = []

for i in myword:
    blankword.append('_')

print(*blankword, sep=' ')

gueses = 0

while True:
    if myword != blankword:

        if gueses < 10:
            checkletter(
                input('Enter letter to check if its within the word: '))
            gueses += 1
            print(10-gueses, 'attemts left.')
        else:
            print('Too many attempts. Try another time.')
            break
    else:
        print('Congratulations!')
        break
