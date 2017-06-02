import random


##TODO: add in phrases/dictionary module of words

def random_word():
    words = ['Shakespeare', 'sound', 'and', 'fury']
    return random.choice(words).upper()






def shannon():
    word = random_word()
    guesses = []
    guessed = False

    print "This word contains", len(word), "letters. \n", len(word) * "_ "

    # TODO: change to guess letters in order
    while (~guessed):
        guess = input("Guess a letter").upper()
        # if guess in guesses:
        #     print "You already guessed", guess, "!"
        # elif len(guess) == len(word):
        #     if guess == word:
        #         guessed = True
        #     else:
        #         guesses.append(guess)
        # elif len()




shannon()



