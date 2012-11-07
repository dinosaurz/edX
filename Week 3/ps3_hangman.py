# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretLetters = []
    for c in secretWord:
        if c in secretLetters:
            continue
        secretLetters.append(c)

    for letter in lettersGuessed:
        if letter in secretLetters:
            secretLetters.remove(letter)
    if len(secretLetters) == 0:
        return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretLetters = [c for c in secretWord]

    for letter in range(len(secretLetters)):
        if not secretLetters[letter] in lettersGuessed:
            secretLetters[letter] = '_'
    return ' '.join(secretLetters)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = [a for a in string.ascii_lowercase]
    for letter in lettersGuessed:
        allLetters.remove(letter)
    return ''.join(allLetters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # All variables
    turnSep = "-" * 13
    guessesLeft = 8
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)

    # First start
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(secretWord), "letters long."
    print turnSep

    # Repeat for each turn
    while True:
        if guessesLeft == 0:
            print "Sorry, you ran out of guesses. The word was", secretWord
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break
        print "You have", guessesLeft, "guesses left."
        print "Available letters:", availableLetters

        guess = raw_input("Please guess a letter: ").lower()
        if len(guess) != 1:
            print turnSep
            continue

        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter:",
        elif not guess in secretWord:
            lettersGuessed.append(guess)
            guessesLeft -= 1
            print "Oops! That letter is not in my word:",
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print "Good guess:",

        availableLetters = getAvailableLetters(lettersGuessed)
        print getGuessedWord(secretWord, lettersGuessed)
        print turnSep

if __name__ == '__main__':
    while True:
        usrCmd = raw_input("Play a game? (y/n) ")
        print ""
        if usrCmd.lower() == 'y':
            secretWord = chooseWord(wordlist).lower()
            hangman(secretWord)
        elif usrCmd.lower() == 'n':
            break
        else:
            continue
