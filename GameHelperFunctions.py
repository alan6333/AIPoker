import random
import copy

class card:
  def __init__(self, suit, number, value):
    self.suit = suit
    self.number = number
    self.value = value

def all_hand_combinations_list(all_cards):
    #7 cards choose 5
    #this method considers every combination of 5 cards in the possible 7 to choose from
    # a helper method for finding the best hand
    all_combos_list = [[all_cards[0], all_cards[1], all_cards[2], all_cards[3], all_cards[4]],\
                        [all_cards[0], all_cards[1], all_cards[2], all_cards[3], all_cards[5]],\
                        [all_cards[0], all_cards[1], all_cards[2], all_cards[3], all_cards[6]],\
                        [all_cards[0], all_cards[1], all_cards[2], all_cards[4], all_cards[5]],\
                        [all_cards[0], all_cards[1], all_cards[2], all_cards[4], all_cards[6]],\
                        [all_cards[0], all_cards[1], all_cards[2], all_cards[5], all_cards[6]],\
                        [all_cards[0], all_cards[1], all_cards[3], all_cards[4], all_cards[5]],\
                        [all_cards[0], all_cards[1], all_cards[3], all_cards[4], all_cards[6]],\
                        [all_cards[0], all_cards[1], all_cards[3], all_cards[5], all_cards[6]],\
                        [all_cards[0], all_cards[1], all_cards[4], all_cards[5], all_cards[6]],\
                        [all_cards[0], all_cards[2], all_cards[3], all_cards[4], all_cards[5]],\
                        [all_cards[0], all_cards[2], all_cards[3], all_cards[4], all_cards[6]],\
                        [all_cards[0], all_cards[2], all_cards[3], all_cards[5], all_cards[6]],\
                        [all_cards[0], all_cards[2], all_cards[4], all_cards[5], all_cards[6]],\
                        [all_cards[0], all_cards[3], all_cards[4], all_cards[5], all_cards[6]],\
                        [all_cards[1], all_cards[2], all_cards[3], all_cards[4], all_cards[5]],\
                        [all_cards[1], all_cards[2], all_cards[3], all_cards[4], all_cards[6]],\
                        [all_cards[1], all_cards[2], all_cards[3], all_cards[5], all_cards[6]],\
                        [all_cards[1], all_cards[2], all_cards[4], all_cards[5], all_cards[6]],\
                        [all_cards[1], all_cards[3], all_cards[4], all_cards[5], all_cards[6]],\
                        [all_cards[2], all_cards[3], all_cards[4], all_cards[5], all_cards[6]]]
    return all_combos_list


def get_player_hand(comm_cards, player_cards):
    #FOR THIS METHOD TO WORK comm_cards HAS TO HAVE 5 CARDS
    #returns ["Hand", strength]


    #a list of all possible cards that make the hand
    all_cards = comm_cards + player_cards 
    #all combinations of 5 that the hand can be (a list of lists of 5 cards)
    all_hand_combinations = all_hand_combinations_list(all_cards)

    #ROYAL FLUSH
    all_hand_combinations_0 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_0:
        if (check_royal_flush(combo)):
            return ["Royal Flush", 14] # Royal flush is only hand possible, wins automatically
        
    #STRAIGHT FLUSH
    #make a list straight_flushes[]
    straight_flushes = []
    #for every combination
    all_hand_combinations_1 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_1:
        combo_copy = copy.deepcopy(combo)
        #check if straight flush
        if (check_straight_flush(combo)):
            #if it is, get strength and add [combo, strength(combo)] to straight_flushes[]
            straight_flushes.append(["Straight Flush", get_hand_strength("Straight Flush", combo_copy)])
    #if there is a straight
    if(len(straight_flushes) > 0):
        #set a 'winner' hand that hasn't been challenged yet, about to challenge            
        sflush_winner = straight_flushes[0]
        #for every straight
        for straight_flush in straight_flushes:
            #if straight_flush[1] (strength) is greater than winner, then winner = straight_flush
            if (straight_flush[1] > sflush_winner[1]):
                sflush_winner = straight_flush
        return sflush_winner #winner is in the form [String hand, int strength]

    #4ofaKIND
    all_hand_combinations_2 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_2:
        #check if 4 of a kind
        if(check_fourofakind(combo)):
            return ["Four of a Kind", 9] #strength is 0 because only one person can get a 4 of a kind in a roun

    #FULL HOUSE
    all_hand_combinations_3 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_3:
        #check for full house
        if(check_fullhouse(combo)):
            return ["Full House", get_hand_strength("Full House", combo)]

    #FLUSH
    all_flushes = []
    all_hand_combinations_4 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_4:
        combo_copy = copy.deepcopy(combo)
        if(check_flush(combo)):
            all_flushes.append(["Flush", get_hand_strength("Flush", combo_copy)])
    if(len(all_flushes) > 0):
        flush_winner = all_flushes[0]
        for flush in all_flushes:
            if (flush[1] > flush_winner[1]):
                flush_winner = flush
        return flush_winner
    
    #STRAIGHT
    all_straights = []
    all_hand_combinations_5 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_5:
        combo_copy = copy.deepcopy(combo)
        if(check_straight_consecutive(combo)):
            all_straights.append(["Straight", get_hand_strength("Straight", combo_copy)])
    if(len(all_straights) > 0):
        straight_winner = all_straights[0]
        for straight in all_straights:
            if (straight[1]>straight_winner[1]):
                straight_winner = straight
        return straight_winner
        
    #THREEOFAKIND
    all_hand_combinations_6 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_6:
        if(check_threeofakind(combo)):
            return ["Three of a Kind", get_hand_strength("Three of a Kind", combo)]
    #TWOPAIR
    all_twopairs = []
    all_hand_combinations_6 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_6:
        combo_copy = copy.deepcopy(combo)
        if(check_twopair(combo)):
            all_twopairs.append(["Two Pair", get_hand_strength("Two Pair", combo_copy)])
    if(len(all_twopairs) > 0):
        tpair_winner = all_twopairs[0]
        for tpair in all_twopairs:
            if (tpair[1]>tpair_winner[1]):
                tpair_winner = tpair
        return tpair_winner

    #PAIR
    all_pairs = []
    all_hand_combinations_7 = copy.deepcopy(all_hand_combinations)
    for combo in all_hand_combinations_7:
        combo_copy = copy.deepcopy(combo)
        if(check_pair(combo)):
            all_pairs.append(["Pair", get_hand_strength("Pair", combo_copy)])
    if(len(all_pairs) > 0):
        pair_winner = all_pairs[0]
        for pair in all_pairs:
            if (pair[1] > pair_winner[1]):
                pair_winner = pair
        return pair_winner

    #HIGHCARD*
    all_highcards = []
    all_hand_combinations_8 = copy.deepcopy(all_hand_combinations)
    #for every combination
    for combo in all_hand_combinations_8:
        #set winner
        combo_highcard = combo[0]
        #loop through current combination
        for card in combo:
            if(int(card.value) > int(combo_highcard.value)):
                combo_highcard = card
        all_highcards.append(combo_highcard)
    if(len(all_highcards)>0):
        best_highcard = all_highcards[0]
        for highcard in all_highcards:
            if(int(highcard.value) > int(best_highcard.value)):
                best_highcard = highcard
        return [best_highcard.number, int(best_highcard.value)]

def check_royal_flush(all_cards):
    suit = all_cards[0].suit
    #same suit
    ace = False
    king = False
    queen = False
    jack = False
    ten = False
    #10-A
    for card in all_cards:
        if (card.suit != suit):
            return False
        if (card.number=="A"):
            ace = True
        if (card.number=="K"):
            king = True 
        if (card.number=="Q"):
            queen = True 
        if (card.number=="J"):
            jack = True
        if (card.number=="10"):
            ten = True

    if(ace and king and queen and jack and ten):
        return True
    return False

def check_straight_flush(all_cards):
    #be a flush
    if(check_flush(all_cards) == False):
        return False
    #numbers/symbols be consecutive
    if(check_straight_consecutive(all_cards) == False):
        return False
    return True

def check_straight_consecutive(combo):
    #THIS ONLY WORKS IF ALL_CARDS IS 5 in length
    cards = sort_little_to_big(combo)
    #try getting a straight by increasing
    #normal straight
    if(int(cards[0].value)+1 == int(cards[1].value) and \
        int(cards[1].value)+1 == int(cards[2].value) and \
        int(cards[2].value)+1 == int(cards[3].value) and \
        int(cards[3].value)+1 == int(cards[4].value)):
        return True
    if (cards[4].number=="A" and \
        cards[0].number=="2" and \
        int(cards[0].value)+1==int(cards[1].value) and \
        int(cards[1].value)+1==int(cards[2].value) and \
        int(cards[2].value)+1==int(cards[3].value)):
            return True
    return False

def check_fourofakind(combo):
    card1 = 'N/A'
    card1number_count = 0
    card2 = 'N/A'
    card2number_count = 0
    for card in combo:
        if (card1 == "N/A"):
            card1 = card
        elif (card2 == "N/A"):
            card2 = card
        elif(card.number == card1.value):
            card1number_count = card1number_count + 1
        elif(card.number == card2.value):
            card2number_count = card2number_count + 1
        else:
            return False # too many numbers/symbols for 4ofakind
    if(card1number_count == 4 or card2number_count == 4):
        return True
    
def check_fullhouse(combo):
    #A A A K K example
    card1 = 'N/A'
    card2 = 'N/A'
    for card in combo:
        if (card1 == "N/A"):
            card1 = card.number
        elif (card2 == "N/A" and card.number != card1):
            card2 = card.number
        elif (card.number == card1):
            continue
        elif (card.number == card2):
            continue
        else: #card.number is a 3rd version so it cant be a full house
            return False
    return True #5 or 4 card1's or card2's not possible, so it has to be 3 or 2 which is a full house at this point
    
def sort_little_to_big(combo):
    in_order = []
    #for every card
    for i in range(5):
        if(combo == []):
            return in_order
        #set cur smallest
        smallest = combo[0]
        #for every card in the combo
        for card in combo:
            #if smallest
            if (int(card.value) < int(smallest.value)):
                smallest = card
        in_order.append(smallest)
        combo.remove(smallest)
    return in_order
    #5 times
        #for every card in combo
            #set winner
            #if it is the smallest
                #set as winner
        #add winner to new list
        #delete winner from og list

def check_flush(all_cards):
    suit = all_cards[0].suit
    for card in all_cards:
        if (card.suit != suit):
            return False
    return True

def check_threeofakind(combo):
    card1 = 'N/A'
    card1_count = 0
    card2 = 'N/A'
    card2_count = 0
    for card in combo:
        if (card1 == "N/A"):
            card1 = card
            card1_count = card1_count + 1
        elif (card2 == "N/A" and card.number != card1.number):
            card2 = card
            card2_count = card2_count + 1
        elif (card.number == card1.number):
            card1_count = card1_count + 1
            continue
        elif (card.number == card2.number):
            card2_count = card2_count + 1
            continue
    if(card1_count == 3 or card2_count == 3):
        return True #return card1 or card2 was 3, return True
    else: #no cards had 3, no three of a kind
        return False
    
def check_twopair(combo):
    # A A 2 2 3
    card1 = "N/A"
    card2 = "N/A"
    card3 = "N/A"
    for card in combo:
        if (card1 == "N/A"):
            card1 = card
        elif (card2 == "N/A" and card.number != card1.number):
            card2 = card
        elif (card3 == "N/A" and card.number != card1.number and card.number != card2.number):
            card3 = card
        elif (card.value == card1.value or card.value == card2.value or card.value == card3.value):
            continue
        else:
            return False
    return True

def check_pair(combo):
    # A K Q J J
    card1 = "N/A"
    card2 = "N/A"
    card3 = "N/A"
    card4 = "N/A"
    for card in combo:
        if (card1 == "N/A"):
            card1 = card
        elif (card2 == "N/A" and card.number != card1.number):
            card2 = card
        elif (card3 == "N/A" and card.number != card1.number and card.number != card2.number):
            card3 = card
        elif (card4 == "N/A" and card.number != card1.number and card.number != card2.number and card.number != card3.number):
            card4 = card
        elif (card.value == card1.value or card.value == card2.value or card.value == card3.value or card.value == card4.value):
            continue
        else:
            return False
    return True
        
def get_hand_strength(hand, combo):
    combo = sort_little_to_big(combo)
    if (hand == "Straight Flush"):
        if(combo[0].value == "2"):
            return 2
        return int(combo[4].value)
    elif(hand == "Full House"):
        return int(combo[4].value)
    elif(hand == "Flush"):
        return int(combo[4].value)
    elif(hand == "Straight"):
        if(combo[0].value == "2"):
            return 2
        return int(combo[4].value)
    elif(hand == "Three of a Kind"):
        card1 = 'N/A'
        card1_count = 0
        card2 = 'N/A'
        card2_count = 0
        card3 = 'N/A'
        card3_count = 0
        for card in combo:
            if (card1 == "N/A"):
                card1 = card
                card1_count = card1_count + 1
            elif (card2 == "N/A" and card.number != card1.number):
                card2 = card
                card2_count = card2_count + 1
            elif (card3 == "N/A" and card.number != card1.number and card.number != card2.number):
                card3 = card
                card3_count = card3_count + 1
            elif (card.number == card1.number):
                card1_count = card1_count + 1
                continue
            elif (card.number == card2.number):
                card2_count = card2_count + 1
                continue
            elif (card.number == card3.number):
                card3_count = card3_count + 1
                continue
        if(card1_count == 3):
            return int(card1.value) #return card1 value
        elif(card2_count == 3): #return card 2 value
            return int(card2.value)
        elif(card3_count == 3):
            return int(card3.value)
        else:
            print("Something went wrong in get_hand_strength() Three of a kind")
            return 0
        
    elif(hand == "Two Pair"):
        #A A K K Q
        card1 = "N/A"
        card1_count = 0
        card2 = "N/A"
        card2_count = 0
        card3 = "N/A"
        card3_count = 0
        for card in combo:
            if (card1 == "N/A"):
                card1 = card
                card1_count = card1_count + 1
            elif (card2 == "N/A" and card.number != card1.number):
                card2 = card
                card2_count = card2_count + 1
            elif (card3 == "N/A" and card.number != card1.number and card.number != card2.number):
                card3 = card
                card3_count = card3_count + 1
            elif (card.value == card1.value):
                card1_count = card1_count + 1
            elif (card.value == card2.value):
                card2_count = card2_count + 1
            elif (card.value == card3.value):
                card3_count = card3_count + 1
            else:
                print("This shouldn't be possible, only 3 unique cards in two pair")
        if(card1_count == card2_count and int(card1.value) > int(card2.value)):
            return int(card1.value)
        if(card1_count == card3_count and int(card1.value) > int(card3.value)):
            return int(card1.value)
        if(card2_count == card1_count and int(card2.value) > int(card1.value)):
            return int(card2.value)
        if(card2_count == card3_count and int(card2.value) > int(card3.value)):
            return int(card2.value)
        if(card3_count == card1_count and int(card3.value) > int(card1.value)):
            return int(card3.value)
        if(card3_count == card2_count and int(card3.value) > int(card2.value)):
            return int(card3.value)
        print("Something went wrong in get_hand_strength()2 Two Pair")
        return
        
    elif(hand == "Pair"):
        # 1 2 3 4 4
        card1 = "N/A"
        card1_count = 0
        card2 = "N/A"
        card2_count = 0
        card3 = "N/A"
        card3_count = 0
        card4 = "N/A"
        card4_count = 0
        for card in combo:
            if (card1 == "N/A"):
                card1 = card
                card1_count = card1_count + 1
            elif (card2 == "N/A" and card.number != card1.number):
                card2 = card
                card2_count = card2_count + 1
            elif (card3 == "N/A" and card.number != card1.number and card.number != card2.number):
                card3 = card
                card3_count = card3_count + 1
            elif (card4 == "N/A" and card.number != card1.number and card.number != card2.number and card.number != card3.number):
                card4 = card
                card4_count = card4_count + 1
            elif (card.value == card1.value):
                card1_count = card1_count + 1
            elif(card.value == card2.value):
                card2_count = card2_count + 1
            elif(card.value == card3.value):
                card3_count = card3_count + 1
            elif(card.value == card4.value):
                card4_count = card4_count + 1
            else:
                print("Something went wrong in get_hand_strength() Pair")
                return -1
        if(card1_count > card2_count and card1_count > card3_count and card1_count > card4_count):
            return int(card1.value)
        elif(card2_count >card1_count and card2_count>card3_count and card2_count > card4_count):
            return int(card2.value)
        elif(card3_count > card1_count and card3_count > card2_count and card3_count > card4_count):
            return int(card3.value)
        elif(card4_count > card1_count and card4_count > card2_count and card4_count > card3_count):
            return int(card4.value)
        else:
            print("Something went wrong in get_hand_strength() Pair")
            return -1
    else:
        print("Something went wrong in get_hand_strength")
        return "Something went wrong in get_hand_strength"

def shuffle_card_deck(card_deck):
    #0-51 Cards
    shuffle_card_deck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #for every card
    for card in card_deck:
        #get random index
        randomIndex = random.randrange(52)
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
    i = 0
    for card in shuffle_card_deck:
        i = i + 1

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