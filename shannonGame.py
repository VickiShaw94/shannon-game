import random


##TODO: add in phrases/dictionary module of words

def random_word():
    words = ['Shakespeare', 'sound', 'and', 'fury']
    return random.choice(words).upper()






def shannon():
    word = random_word()
    guesses = []
    print "This word contains", len(word), "letters. \n", len(word) * "_"


shannon()



