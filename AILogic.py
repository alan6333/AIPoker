import copy
from GameHelperFunctions import get_player_hand

class Card:
  def __init__(self, suit, number, value):
    self.suit = suit
    self.number = number
    self.value = value

  def printCard(self):
    print(self.suit + " " + self.number)

def format_money_to_bet(money_to_bet, current_bet):
   '''
   This method is to package the AI's decision for the function that needed the AI's input
   '''
   #+50 is because it's kinda redundant to bet a small amount more than current bet
   #if you don't want to bet more than the current bet => FOLD
   if (money_to_bet < current_bet):
      return "2"
   #if you want to bet exactly the current bet => CHECK
   if (money_to_bet <= current_bet + 50):
      return "3"
   #if you want to bet more than the current bet => RAISE
   if (money_to_bet > current_bet + 50):
      return "4 " + str(int(money_to_bet))

def player_money_multiplier_evaluator(player_money):
    '''
    The less money you have => the more you bet (more risk)
    The more money you have => the less you bet (less risk)
    Each player starts off with 2900 dollars.
    Which means if you win completely you can have 5800 dollars
    If you lose then you have 0 dollars

    Our return multiplier will be between 0 and 1, 0% of your $ or 100% of your money
    '''
    player_fraction_of_money = player_money/5800 
    #subtract from 1 to make the losing player more risky not the winner
    #multiply result by .7 to make overall bet less harsh
    multiplier = 1 - player_fraction_of_money
    return multiplier

def hand_confidence_eval_helper(hand, flop):
   hand_mult = 0
   strength_mult = 0
   '''
   Helper function for confidence_multiplier_evaluator().
   Once you have the current hand/strength of the player and the current flop,
   we can assign it a multiplier based on how "strong" it is.

   hand score * flop score = hand confidence multiplier
   Parameters:
   ["Hand", strength], and flop
   '''
   #PREFLOP
   if(flop==0):
      if(hand[0] == "Pair"):
        hand_mult = .1
      else:
        hand_mult = .05
   #FLOP
   if(flop==3 or flop ==4 or flop == 5):
      if(hand[0] == "Royal Flush"):
        hand_mult = 1
      if(hand[0] == "Straight Flush"):
        hand_mult = .9
      if(hand[0] == "Four of a Kind"):
        hand_mult = .7
      if(hand[0] == "Full House"):
        hand_mult = .6
      if(hand[0] == "Flush"):
        hand_mult = .5
      if(hand[0] == "Straight"):
        hand_mult = .4
      if(hand[0] == "Three of a Kind"):
        hand_mult = .3
      if(hand[0] == "Two Pair"):
        hand_mult = .2
      if(hand[0] == "Pair"):
        hand_mult = .1
      else:
        hand_mult = .05

   strength_mult = (hand[1]/14) * .01 #mult .1 so confidence doesn't surpass a better hand
   if(hand_mult + strength_mult > 1): #rf
      return 1
   else:
      return hand_mult + strength_mult

def hand_confidence_multiplier_evaluator(player_cards, comm_cards_dc):
    comm_cards = copy.deepcopy(comm_cards_dc)

    #if PREFLOP (up to a pair)
    if(len(comm_cards) == 0):
        comm_cards.append(Card("aa", "aa", -11))
        comm_cards.append(Card("bb", "bb", -22))
        comm_cards.append(Card("cc", "cc", -33))
        comm_cards.append(Card("dd", "dd", -44))
        comm_cards.append(Card("ee", "ee", -55))
    #if FLOP (up to a royal flush)
    elif(len(comm_cards) == 3):
        comm_cards.append(Card("ff", "ff", -66))
        comm_cards.append(Card("gg", "gg", -77))
    #if TURN (up to a royal flush)
    elif(len(comm_cards) == 4):
        comm_cards.append(Card("hh", "hh", -88))

    hand = get_player_hand(comm_cards, player_cards)
    return hand_confidence_eval_helper(hand, len(comm_cards))


def ai_make_decision(player_cards, comm_cards, player_money, current_bet):
    '''
    To make the best AI decision maker we would either need to implement 
    Counterfactual Regret Minimization which is outside the scope of this course or
    the expensive method of evaluating the get_player_hand() algorithm
    for 52choose7 where 2 of the 7 are known which is too computationally expensive.
    So instead I made a modified version of the 2nd method: since my game forces
    the game to head to the River Round (where are comm cards are known), this forces the 
    amount of combinations to become to 21 which is feasible. All of the other rounds
    confidence level is evaluated by taking into account the players money and the current hand and
    strength of the player.

    Parameters are:
    player_cards[], comm_cards[], player.money, flop
    RETURN LOOKS LIKE EITHER: 2 (for fold), 3 (for check), 4 amount (for bet_amount)
    Bets depending on players money and hand
    if confident, bets more. if not then bet less
    confidence depends on player money and hand (if they less $$$ then player more risky, if you have more bet more conservative) 
    (stong hand => more risky, weak hand => less risky)
    confidence also depends on current cards in your hand
    player.money * player_money multiplier * confidence multiplier = ai move (after formatting into return form)
    '''

    player_money_multiplier = player_money_multiplier_evaluator(player_money)
    confidence_multiplier = hand_confidence_multiplier_evaluator(player_cards, comm_cards)

    money_to_bet = player_money * player_money_multiplier * confidence_multiplier

    
    return format_money_to_bet(money_to_bet, current_bet)