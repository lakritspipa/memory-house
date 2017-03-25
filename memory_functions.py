# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 18:26:46 2016

@author: JoaJoh
"""

import random
deckSize = 12

class Cards(object):
    """ 
    Memory card to be used in the game.
    The card has a frontside and a backside, and can be flipped over.
    """
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def getFront(self):
        return self.front

    def getBack(self):
        return self.back

    def flipCard(self):
        temp = self.getFront()
        self.front = self.getBack()
        self.back = temp

    def __eq__(self, other):
        return self.getFront == other.getFront
    
    def __str__(self):
        return '|' + str(self.getFront()) + '/' + str(self.getBack()) + '|'
    
    def __repr__(self):
        return 'Cards(%s,%s)' % (self.getFront(), self.getBack())

def loadLetters():
    """ Creats a list of the letter in the alphabet """ 
    import string
    alphaStr = string.ascii_lowercase
    alphabet = []
    for letter in alphaStr:
        alphabet.append(letter)
    return alphabet

def randomLetters(alphabet, deckSize):
    """
    Returns a list of random letters.
    alphabet is a array of the letters in the alphabet.
    deckSize is an int, representing the number of letters to return
    """
    randLetters = []
    count = 0
    while count < deckSize:
        select = random.choice(alphabet)
        if select not in randLetters:
            randLetters.append(select)
            count += 1
    random.shuffle(randLetters)
    return randLetters

def createCards(randomLetters):
    """ 
    Returns a deck of game cards in the form of a dictionary.
    deckSize is an int. 
    """
    gameCards = {}
    for i in range(len(randomLetters)):
        gameCards['card' + str(i)] = Cards(randomLetters[i], 'O')
    return gameCards

def printBoard(gameCards):
    """Prints out game board"""
    #board = []
    #count = 0
    for row in gameCards.keys():
        print(gameCards[row])

#  for row in board:
#        print("   ".join(row))


def loadWords():
    """
    This function creates and returns a list full of words
    """
    print("Loading words from file...")
    in_file = open(wordlist_file, "r")
    one_long_string = in_file.readline()
    wordlist = one_long_string.split()
    in_file.close()
    return wordlist
    
def randomWords(wordlist, deckSize):
    """
    Returns a list of random words. wordList is a array of words.
    deckSize is an int, representing the number of words to return
    """
    randomWords = []
    for item in range(deckSize):
        select = random.choice(wordlist)
        randomWords.append(select)
        randomWords.append(select)
    return randomWords

#wordlist_file = input("Enter file name of file containing words: ")
#wordlist = loadWords()
#choosen_words = selectWords()
#print(choosen_words)
