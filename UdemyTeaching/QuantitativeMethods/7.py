'''
Demonstration of randomness of random.shuffle on list of objects
'''
import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def initializeDeck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace', '2', '3','4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    cards = []
    for suit in suits:
        for rank in ranks:
            card = Card(suit, rank)
            cards.append(card)
    return cards
def printSpecial(cards):
    for i in range(len(cards)):
        print('{',cards[i].suit,cards[i].rank,'}',end = " ")
    print(' ')
    print('------------------------------------------------------')
def shuffleThenPrint(cards):
    random.shuffle(cards)
    printSpecial(cards)

'''
 for card in cards:
 print('{0} of {1}'.format(card.rank, card.suit))
'''

if __name__ == '__main__':
    print(__doc__)
    cards = initializeDeck()
    shuffleThenPrint(cards)
    shuffleThenPrint(cards)
    shuffleThenPrint(cards)