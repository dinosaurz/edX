from ps4a import *


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all possible
    permutations of lengths 1 to HAND_SIZE.

    If all possible permutations are not in wordList, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    bestScore, bestWord = 0, None

    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, HAND_SIZE)
            if score > bestScore:
                bestScore, bestWord = score, word
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    """
    lettersLeft = HAND_SIZE
    totalScore = 0

    while lettersLeft > 0:
        print "Current Hand:",
        displayHand(hand)

        word = compChooseWord(hand, wordList)
        if word is None:
            break
        else:
            wordScore = getWordScore(word, HAND_SIZE)
            totalScore += wordScore
            print '"' + word + '" earned', str(wordScore), "points. Total:", str(totalScore), "points"

            hand = updateHand(hand, word)
            lettersLeft = calculateHandlen(hand)

    if lettersLeft == 0:
        print "Run out of letters. Total score:", totalScore, "points"
    else:
        print "Goodbye! Total score:", totalScore, "points"


#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = None
    while True:
        # Determine what the hand is
        userCmd = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if userCmd == 'n':
            hand = dealHand(HAND_SIZE)
        elif userCmd == 'r':
            if hand is None:
                print "You have not played a hand yet. Please play a new hand first!"
                continue
        elif userCmd == 'e':
            break
        else:
            print "Invalid Command"
            continue

        # Play the game itself
        while True:
            userCmd = raw_input("Enter u to play as a user, c to play as a computer: ")
            if userCmd == 'u':
                playHand(hand.copy(), wordList, HAND_SIZE)
                break
            elif userCmd == 'c':
                compPlayHand(hand.copy(), wordList)
                break
            else:
                print "Invalid Command"
                continue
        print

    # finished
    print


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

    print "Goodbye!"
