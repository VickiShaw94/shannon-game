import random


##TODO: add in phrases/dictionary module of words

def random_word():
    words = ['Shakespeare', 'sound', 'and', 'fury']
    return random.choice(words).upper()






def shannon():
    word = random_word()
    guesses = [] # letters guessed
    tryNum = [] # counter tracker

    print "This word contains", len(word), "letters. \n", len(word) * "_ "


    # TODO: change to guess letters in order
    for letter in word:
        guessNum = 0
        guessed = False
        while ~guessed:
            guess = raw_input("Guess the letters of the word in order \n").upper()
            if len(guess) > 1:
                print "Please enter one letter at a time."
            elif len(guess) == 0:
                print "Please guess one letter"
            elif ~(guess == letter):
                if ~(guess in guesses):
                    guessNum += 1
                    guesses.append(guess)
                    print "Guess again! \nGuess count:", guessNum
                else:
                    print "You already guessed that! Try again"
            else: # correct letter guessed
                guessed = True
                tryNum.append(guessNum)


        # if guess in guesses:
        #     print "You already guessed", guess, "!"
        # elif len(guess) == len(word):
        #     if guess == word:
        #         guessed = True
        #     else:
        #         guesses.append(guess)
        # elif len()




shannon()



