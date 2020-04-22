import random


def get_word():
    words = open('words.txt').read().splitlines()
    return list(random.choice(words).upper())


def get_attempts():
    while True:
        num_attempts = input(
            'How many attempts would you like to have? (1-30) ')
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 30:
                return num_attempts
            else:
                print('{} is not number beetween 1 and 30.'.format(num_attempts))
        except ValueError:
            print('{} is not number beetween 1 and 30.'.format(num_attempts))


def check_for_letter(guess, word, blankword):
    matches = 0
    for i in range(len(word)):
        if guess[0] == word[i]:
            blankword[i] = guess[0]
            matches += 1

    if matches == 0:
        print('Sorry, the word does not contain letter ', guess[0], '.')
    elif matches == 1:
        print('Yes! The word contains letter ', guess[0], '.')
    else:
        print('Yes! The word contains ', matches, guess[0], '.')


def play_hangman():
    word = get_word()
    # print(''.join(word))            # uncomment to see the hidden word
    num_attempts = get_attempts()
    blankword = ['_' for i in word]
    print("Word you're guessing has", len(word),
          "letters. You have {} attempts. Good luck!".format(num_attempts))
    print(*blankword)
    guesses = []

    while True:
        guess = input(
            'Please enter one letter or {}-letter word: '.format(len(word)))
        guess = list(guess.upper())
        if guess in guesses:
            print('You have already guessed "', guess[0], '".')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                print('Cogngarulation! The word is ', ''.join(word),
                      '! It took you ', len(guesses), 'tries.')
                return False
            else:
                print('Sorry, that is not correct.')
        elif len(guess) == 1 and guess[0].isalpha():
            guesses.append(guess)
            check_for_letter(guess, word, blankword)
            print(*blankword)

        else:
            print('Incorrect input.')

        if blankword == word:
            print('Cogngarulation! The word is ', ''.join(word),
                  '! It took you ', len(guesses), 'tries.')
            return False

        if len(guesses) >= num_attempts:
            print('Sorry, you have reached limit of {} attemts. The word is '.format(
                num_attempts), ''.join(word), '. Try next time.')
            return False


play_hangman()
