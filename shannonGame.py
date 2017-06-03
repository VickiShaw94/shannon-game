import random


##TODO: add in phrases/dictionary module of words

def random_word():
    """

    :return: string random_word
    """
    words = ['Shakespeare', 'sound', 'and', 'fury']
    return random.choice(words).upper()

def shannon():
    word = random_word()
    tryNum = [] # counter tracker

    progress = ""
    startString = "_ " * len(word)
    print "This word contains", len(word), "letters. Start guessing! \n"

    # TODO: change to dictionary
    for i, str in enumerate(word):
        guessNum = 0
        guessed = False
        guesses = [] # letters guessed

        while ~guessed:
            guess = raw_input(startString + "\n").upper()

            if len(guess) > 1:
                print "Please enter one letter at a time."

            elif len(guess) == 0:
                print "Please guess one letter"

            # if valid input, but not the correct letter
            elif (guess != str):
                if ~(guess in guesses):
                    guessNum += 1
                    guesses.append(guess)
                    print "Guess again! \nGuess count:", guessNum

                else:
                    print "You already guessed that! Try again"

            else: # correct letter guessed
                guessed = True
                tryNum.append(guessNum + 1)

                startString[i] = str
                print "Good guess! \n", startString, "\n", tryNum



shannon()



