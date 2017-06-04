import random


##TODO: add in phrases/dictionary module of words

def random_word():
    """
    randomly selects a word
    :return: string random_word
    """
    words = ['Shakespeare', 'sound', 'and', 'fury']
    return random.choice(words).upper()



def guess_check(word):
    """
    iterates through each letter in the word, checks against user prompted guess
    stores items in a dictionary
    :param word: random word selected to be guessed

    """

    # initializes empty guess string
    progressStr = ["_ "] * len(word)
    tryNum = []

    for i, s in enumerate(word):
        guessNum = 0
        guessed = False
        guesses = [] # letters guessed

        while ~guessed:
            print " " .join(progressStr)
            guess = raw_input("\n").upper()

            if len(guess) > 1:
                print "Please enter one letter at a time."

            elif len(guess) == 0:
                print "Please guess one letter"

            # if valid input, but not the correct letter
            elif (guess != s):
                if ~(guess in guesses):
                    guessNum += 1
                    guesses.append(guess)
                    print "Guess again! \nGuess count:", guessNum

                else:
                    print "You already guessed that! Try again"

            else: # correct letter guessed
                guessed = True
                tryNum.append(guessNum + 1)

                progressStr[i] = s
                print "Good guess! \n" + "".join(map(str, tryNum))



def shannon():
    word = random_word()
    print "This word contains", len(word), "letters. Start guessing! \n"
    guess_check(word)


shannon()



