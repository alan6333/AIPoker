import random

class card:
  def __init__(self, suit, number, value):
    self.suit = suit
    self.number = number
    self.value = value


def shuffle_card_deck(card_deck):
    #0-51 Cards
    shuffle_card_deck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #for every card
    for card in card_deck:
        #get random index
        randomIndex = random.randrange(51)
        #if index is not taken, put the card there
        if (shuffle_card_deck[randomIndex]==0):
            shuffle_card_deck[randomIndex] = card
        else:
           #while we're at a spot that is taken
           while(shuffle_card_deck[randomIndex]!=0):
                #shift the index, account for edge case
                if (randomIndex == 51):
                    randomIndex = 0
                else:
                   randomIndex = randomIndex + 1
                #if the index is not taken this time then take it, else it loop until all cards are shuffled
                if (shuffle_card_deck[randomIndex]==0):
                    shuffle_card_deck[randomIndex] = card
                    break
    ia = 0
    for card in shuffle_card_deck:
        print(str(ia) + ' ' + str(shuffle_card_deck[ia].suit) + str(shuffle_card_deck[ia].number))
        ia = ia + 1

    return shuffle_card_deck


def make_card_deck(card_deck):
    card_deck.append(card('hearts', '2', '2'))
    card_deck.append(card('hearts', '3', '3'))
    card_deck.append(card('hearts', '4', '4'))
    card_deck.append(card('hearts', '5', '5'))
    card_deck.append(card('hearts', '6', '6'))
    card_deck.append(card('hearts', '7', '7'))
    card_deck.append(card('hearts', '8', '8'))
    card_deck.append(card('hearts', '9', '9'))
    card_deck.append(card('hearts', '10', '10'))
    card_deck.append(card('hearts', 'J', '11'))
    card_deck.append(card('hearts', 'Q', '12'))
    card_deck.append(card('hearts', 'K', '13'))
    card_deck.append(card('hearts', 'A', '14'))
    card_deck.append(card('clubs', '2', '2'))
    card_deck.append(card('clubs', '3', '3'))
    card_deck.append(card('clubs', '4', '4'))
    card_deck.append(card('clubs', '5', '5'))
    card_deck.append(card('clubs', '6', '6'))
    card_deck.append(card('clubs', '7', '7'))
    card_deck.append(card('clubs', '8', '8'))
    card_deck.append(card('clubs', '9', '9'))
    card_deck.append(card('clubs', '10', '10'))
    card_deck.append(card('clubs', 'J', '11'))
    card_deck.append(card('clubs', 'Q', '12'))
    card_deck.append(card('clubs', 'K', '13'))
    card_deck.append(card('clubs', 'A', '14'))
    card_deck.append(card('diamond', '2', '2'))
    card_deck.append(card('diamond', '3', '3'))
    card_deck.append(card('diamond', '4', '4'))
    card_deck.append(card('diamond', '5', '5'))
    card_deck.append(card('diamond', '6', '6'))
    card_deck.append(card('diamond', '7', '7'))
    card_deck.append(card('diamond', '8', '8'))
    card_deck.append(card('diamond', '9', '9'))
    card_deck.append(card('diamond', '10', '10'))
    card_deck.append(card('diamond', 'J', '11'))
    card_deck.append(card('diamond', 'Q', '12'))
    card_deck.append(card('diamond', 'K', '13'))
    card_deck.append(card('diamond', 'A', '14'))
    card_deck.append(card('spades', '2', '2'))
    card_deck.append(card('spades', '3', '3'))
    card_deck.append(card('spades', '4', '4'))
    card_deck.append(card('spades', '5', '5'))
    card_deck.append(card('spades', '6', '6'))
    card_deck.append(card('spades', '7', '7'))
    card_deck.append(card('spades', '8', '8'))
    card_deck.append(card('spades', '9', '9'))
    card_deck.append(card('spades', '10', '10'))
    card_deck.append(card('spades', 'J', '11'))
    card_deck.append(card('spades', 'Q', '12'))
    card_deck.append(card('spades', 'K', '13'))
    card_deck.append(card('spades', 'A', '14'))
    return card_deck