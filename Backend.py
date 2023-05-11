from GameHelperFunctions import make_card_deck, shuffle_card_deck, get_player_hand
import GameHelperFunctions
import time, random, pygame, sys

#
# This class makes a Card 'Object'
#
class Card:
  def __init__(self, suit, number, value):
    self.suit = suit
    self.number = number
    self.value = value

  def printCard(self):
    print(self.suit + " " + self.number)
  
#
# This class makes a player 'Object'
#
class Player:
   def __init__(self, id):
      self.money = 2900
      self.blind = "Undecided"
      self.cards = [0,0]
      self.move = "NA"
      self.player_id = id

#
# This class is the backend, keeps track of the game logic
#
class GameModel():
    def __init__(self):
       self.gamemode = "N/A" # default vs AI
       self.game_state = "start" 
       self.pot = 0 #pot of money
       self.utg = "Undecided" #UTG means the player next to the dealer, they always start the bet
       self.second_better = "Undecided" #only 2 player so there is only one other better
       self.p1 = Player("Player 1") 
       self.p2 = Player("Player 2")
       self.message_to_user = "Welcome to AI Poker by Alan Coronado" # this var is what the frontend uses to print
       self.card_deck = [] 
       self.flop = 0
       self.comm_cards = []
       self.bet = 0
       self.getting_input = False
       self.input_bet_choice = "N/A"

    #game config method
    def config_game(self):

        #change game state
        self.game_state = "reset_round"
        #randomize blinds
        self.randomize_blinds()
        return
    
    def progress_game(self):
      if self.game_state == 'reset_round':
          self.reset_round()
          return

      elif self.game_state == "blinds_bet": 
          self.blinds_bet()
          if(self.game_state == 'leave'):
             return
          self.game_state = "BETTING_show_comm_cards_utg"
          return
      elif self.game_state[0:7] == "BETTING":
         #bet here
         self.betting(self.input_bet_choice)
         return

      elif self.game_state == "leave":
          self.leave()
          return
      elif self.game_state == "quit":
          quit()
      else:
         return
        
        
    def get_message_to_user(self):
      return self.message_to_user
    
    def get_gamemode(self):
      return self.gamemode 
    
    def randomize_blinds(self):
      randomNum = random.randrange(2)
      if (randomNum == 0):
         self.p1.blind = "PreBig"
         self.second_better = self.p1
         self.p2.blind = "PreSmall"
         self.utg = self.p2
      else:
         self.p1.blind = "PreSmall"
         self.utg = self.p1
         self.p2.blind = "PreBig"
         self.second_better = self.p2
      return
    
    def deal_2_cards(self, player):
      #card 1
      randomIndex1 = random.randrange(len(self.card_deck))
      player.cards[0] = self.card_deck[randomIndex1]
      self.card_deck.pop(randomIndex1)
      #card 2
      randomIndex2 = random.randrange(len(self.card_deck))
      player.cards[1] = self.card_deck[randomIndex2]
      self.card_deck.pop(randomIndex2)

    def pull_comm_card(self, amount):
       for i in range(amount):
         #card 1
         randomIndex = random.randrange(len(self.card_deck))
         self.comm_cards.insert(len(self.comm_cards), self.card_deck[randomIndex])
         self.card_deck.pop(randomIndex)
      
    def show_comm_cards(self):
       #preflop
       if(len(self.comm_cards) == 0):
          self.message_to_user = "\nPREFLOP ========================================================================"
       #flop
       elif(len(self.comm_cards) == 3):
            self.message_to_user = "\nFLOP ========================================================================\nCommunity deck is: " + self.comm_cards[0].suit + "-" + self.comm_cards[0].number + " | "\
               + self.comm_cards[1].suit + "-" + self.comm_cards[1].number + " | "\
               + self.comm_cards[2].suit + "-" + self.comm_cards[2].number + "\n"
       #turn
       elif(len(self.comm_cards) == 4):
            self.message_to_user = "\nTURN ========================================================================\nCommunity deck is: " + self.comm_cards[0].suit + "-" + self.comm_cards[0].number + " | "\
            + self.comm_cards[1].suit + "-" + self.comm_cards[1].number + " | "\
            + self.comm_cards[2].suit + "-" + self.comm_cards[2].number + " | "\
            + self.comm_cards[3].suit + "-" + self.comm_cards[3].number + "\n"
       #river
       else:
            self.message_to_user = "\nRIVER ========================================================================\nCommunity deck is: " + self.comm_cards[0].suit + "-" + self.comm_cards[0].number + " | "\
            + self.comm_cards[1].suit + "-" + self.comm_cards[1].number + " | "\
            + self.comm_cards[2].suit + "-" + self.comm_cards[2].number + " | "\
            + self.comm_cards[3].suit + "-" + self.comm_cards[3].number + " | "\
            + self.comm_cards[4].suit + "-" + self.comm_cards[4].number + "\n"
       return self.message_to_user
    
    def get_big_blind(self):
       if(self.p1.blind == "Big"):
          return "Player 1"
       else:
          return "Player 2"
       
    def get_small_blind(self):
        if(self.p1.blind == "Small"):
          return "Player 1"
        else:
          return "Player 2"
    
    def get_utg(self):
       if(self.utg == self.p1):
          return "Player 1"
       elif (self.utg == self.p2):
          return "Player 2"
       else:
          return "UTG is Undecided"
    
    def get_second_bet(self):
       if (self.second_better == self.p1):
          return "Player 1"
       elif (self.second_better == self.p2):
          return "Player 2"
       else:
          return "2nd Better is Undecided"
    
    def get_player_money(self, player):
       return player.money
       
    def get_winner(self):
         if(self.p1.money > self.p2.money):
            return "Player 1 is the winner!"
         elif (self.p2.money < self.p1.money):
            return "Player 2 is the winner!"
         else:
            return "It is a tie!"
       
    def show_player_hand(self, player):
      return "Your cards are: \n" + player.cards[0].number + "-" +  player.cards[0].suit + " " + player.cards[1].number + "-" +  player.cards[1].suit
    
    def blinds_bet(self):
       p1_bet = 0
       p2_bet = 0
       #p1 is Big blind
       if (self.p1.blind=="Big"):
          p1_bet = 50
          p2_bet = 25
       else: #p1 is small blind
          p1_bet = 25
          p2_bet = 50
       #P1 and P2 have no money
       if (self.p1.money < p1_bet and self.p2.money < p2_bet):
          self.message_to_user += "Player 1 & p2 have no money" + "Its a tie, the game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n"
          self.game_state = "leave"
       #P1 has no money
       elif (self.p1.money < p1_bet and self.p2.money >= p2_bet):
          self.message_to_user += "Player 1 has no money" + "Player 2 wins! The game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n"
          self.game_state = "leave"
       #P2 has no money
       elif (self.p1.money >= p1_bet and self.p2.money < p2_bet):
          self.message_to_user += "Player 2 has no money" + "Player 1 wins! The game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n"
          self.game_state = "leave"
       #everyone has money, do the bets
       else:
          self.p1.money = self.p1.money - p1_bet
          self.p2.money = self.p2.money - p2_bet
          self.pot = self.pot + p1_bet + p2_bet
          self.message_to_user = "Player 1 is " + self.p1.blind + " blind & bet $" + str(p1_bet) + "!\n"\
          + "Player 2 is " + self.p2.blind + " blind & bet $" + str(p2_bet) + "!\n"\
          + self.get_utg() + " is 'Under The Gun' with $" + str(self.get_player_money(self.utg)) +" dollars.\n"
   
    def switch_blinds(self):
         #switch blinds for next round
          if (self.p1.blind == "Small"):
             self.p1.blind = "Big"
             self.p2.blind = "Small"
          elif (self.p1.blind == "Big"):
             self.p1.blind = "Small"
             self.p2.blind = "Big"
          elif (self.p1.blind[:3] == "Pre"):
             self.p1.blind = self.p1.blind[3:]
             self.p2.blind = self.p2.blind[3:]
             return
         
    def get_gamestate(self):
       return self.game_state
       
    def if_awaiting_input(self):
       return self.getting_input
    
    def set_awaiting_input(self, bool):
       self.getting_input = bool
       return
    
    def input_bet(self, input):
       self.input_bet_choice = input
       return

    
    def get_flop(self):
       flop = "Preflop"
       #preflop
       if(len(self.comm_cards) == 0):
          flop = "Preflop"
       #flop
       elif(len(self.comm_cards) == 3):
            flop = "Flop"
       #turn
       elif(len(self.comm_cards) == 4):
            flop = "Turn"
       #river
       else:
            flop = "River"
       return flop

    def get_pot(self):
       return self.pot
    
    def get_player_cash(self, player):
       if(player == "p1"):
          return self.p1.money
       else:
          return self.p2.money
       
#======================================================================================================================
    def leave(self):
       self.game_state = "quit"
       self.message_to_user = self.get_utg() + " left the table, game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
         + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n" + self.get_winner()
       return
    
    def showdown(self):
       #if there are not 5 cards in the community deck
       if (self.comm_cards != 5):
          times_to_draw = 5 - len(self.comm_cards)
          for i in range(times_to_draw):
            self.pull_comm_card(1)
             
       #reset the round
       self.game_state = "reset_round"
       #showdown the cards and see who wins
       self.message_to_user = "\nPot is $" + str(self.pot)
       p1_hand = get_player_hand(self.comm_cards, self.utg.cards)
       p2_hand = get_player_hand(self.comm_cards, self.second_better.cards)
       #P1 BY HAND
       if(self.hand_score(p1_hand[0]) > self.hand_score(p2_hand[0])):
          self.p1.money = self.p1.money + self.pot
          self.message_to_user = self.message_to_user + "\nP1 has a " + p1_hand[0] + "\nP2 has a " + p2_hand[0] + ".\n"\
            + "P1 wins the hand. The pot goes to P1 $" + str(self.pot) + ".\n"\
            + "\nNEXT ROUND\n"
          return
       #P2 BY HAND
       elif(self.hand_score(p1_hand[0]) < self.hand_score(p2_hand[0])):
          self.p2.money = self.p2.money + self.pot
          self.message_to_user = self.message_to_user + "\nP1 has a " + p1_hand[0] + "\nP2 has a " + p2_hand[0] + ".\n"\
            + "P2 wins the hand. The pot goes to P2 $" + str(self.pot) + ".\n"\
            + "\nNEXT ROUND\n"
          return
       #TIEBREAKER
       else: #tie
            #p1 by tiebreaker
            if(p1_hand[1] > p2_hand[1]):
                  self.p1.money = self.p1.money + self.pot
                  self.message_to_user = self.message_to_user + "\nP1 has a " + p1_hand[0] + "\nP2 has a " + p2_hand[0] + ".\n"\
                     + "P1 wins the tiebreaker. The pot goes to P1 $" + str(self.pot) + ".\n"\
                     + "\nNEXT ROUND\n"
                  return
            #p2 by tiebreaker
            elif(p2_hand[1] > p1_hand[1]):
               self.p2.money = self.p2.money + self.pot
               self.message_to_user = self.message_to_user + "\nP1 has a " + p1_hand[0] + "\nP2 has a " + p2_hand[0] + ".\n"\
                  + "P2 wins the tiebreaker. The pot goes to P2 $" + str(self.pot) + ".\n"\
                  + "\nNEXT ROUND\n"
               return
            #tie - split
            else:
               self.p1.money = self.p1.money + (self.pot/2)
               self.p2.money = self.p2.money + (self.pot/2)
               self.message_to_user = self.message_to_user + "\nP1 has a " + p1_hand[0] + "\nP2 has a " + p2_hand[0] + ".\n"\
                  + "It is a tie! The pot is split $" + str(self.pot/2) + " each.\n"\
                  + "\nNEXT ROUND\n"
               return
       
    def hand_score(self, hand):
       if(hand == "Royal Flush"):
          return 10
       elif(hand == "Straight Flush"):
          return 9 
       elif(hand == "Four of a Kind"):
          return 8
       elif(hand == "Full House"):
          return 7 
       elif(hand == "Flush"):
          return 6 
       elif(hand == "Straight"):
          return 5
       elif(hand == "Three of a Kind"):
          return 4
       elif(hand == "Two Pair"):
          return 3
       elif(hand == "Pair"):
          return 2
       else: #Highcard?
          return 1

    def ask_user_for_gamemode(self):
        self.message_to_user = "Welcome to AI Poker by Alan Coronado\nThe dealer is shuffling cards...\n\n" \
         + "Please choose your opponent! "
        return
    
    def choose_logistics(self, uinput):
      self.gamemode = uinput
      if (uinput == "AI"):
          self.message_to_user = "\n\nReady to play against: AI!\nThe Dealer is done Shuffling\n"
          self.gamemode = "AI"
      elif (uinput == "Human"):
          self.message_to_user = "\n\n\nReady to play against: Human!\nThe Dealer is done shuffling.\n"
          self.gamemode = "Human"
      else:
          self.message_to_user = "\nInvalid input, try again.\nPlease a VALID opponent, type 'AI' or 'Human': "   
      return
    
    def reset_round(self):
       
       #reset card deck
       self.card_deck = [] 
       self.card_deck = make_card_deck(self.card_deck)
       self.card_deck = shuffle_card_deck(self.card_deck)
       #empty player hand
       self.p1.cards = [0,0]
       self.p2.cards = [0,0]
       #reset players moves
       self.p1.move = "NA"
       self.p2.move = "NA"
       #empty comm card list
       self.comm_cards = []
       #deal 2 cards
       self.deal_2_cards(self.p1)
       self.deal_2_cards(self.p2)
       # empty pot
       self.pot = 0
       #reset bet
       self.bet = 50
       #reset flop
       self.flop = 0
       #switch utg
       if(self.utg == self.p1):
          self.utg = self.p2
          self.second_better = self.p1
       else:
          self.utg = self.p1
          self.second_better = self.p2
       #switch blinds
       self.switch_blinds()
       self.game_state = "blinds_bet"
       self.message_to_user = "Round begins...\nDealt two cards to each player...\n"

    def betting(self, input):
      #SHOW X COMMUNITY CARDS
      if (self.game_state == "BETTING_show_comm_cards_utg"):
         if (self.flop == 0): #Preflop
            #show no cards
            time.sleep(0)
         elif (self.flop == 1): #Flop
            #show 3 card
            self.pull_comm_card(3)
         elif (self.flop == 2): #Turn
            #show 1 card
            self.pull_comm_card(1)
         elif (self.flop == 3): #River
            #show 1 card
            self.pull_comm_card(1)
         else:
            #something went wrong
            self.game_state = "leave"
            return
         self.bet = 0
         
         if(self.gamemode=="Human"):
            #do human
            self.game_state = "BETTING_warn_showUTG_cards"
         else:
            #do AI
            self.game_state = "BETTING_showUTG_cards"
         self.message_to_user = "Showing community deck!\n"
      #UTG
      if (self.game_state == "BETTING_warn_showUTG_cards"): #Human
         self.game_state = "BETTING_showUTG_cards"
         self.message_to_user = "Showing " + self.utg.player_id + " cards in 5 seconds...\n\n\n"    
         return
      if (self.game_state == "BETTING_showUTG_cards"):            
         self.game_state = "BETTING_betUTG"
         self.show_cards(self.utg, self.utg.blind)
         self.show_player_hand(self.utg)
         self.getting_input = True
         return
      if (self.game_state == "BETTING_betUTG"):
         # if(self.getting_input != True):
         if(input == "N/A"):
            return
         self.utg_bet(input)
         self.input_bet_choice = "N/A"
         self.getting_input = False
         return
         # return
      #Second Better
      if (self.game_state == "BETTING_warn_show2nd_cards"): #Human
         self.game_state = "BETTING_show2nd_cards"
         self.message_to_user = "Showing " + self.second_better.player_id + " cards in 5 seconds...\n\n\n"
         return
      if (self.game_state == "BETTING_show2nd_cards"):
         self.game_state = "BETTING_bet2nd"
         self.show_cards(self.second_better, self.second_better.blind)
         self.show_player_hand(self.second_better)
         self.getting_input = True
         return
      if (self.game_state == "BETTING_bet2nd"):
         # if(self.getting_input == True):
         if(input == "N/A"):
            return
         self.second_bet(input)
         self.input_bet_choice = "N/A"
         self.getting_input = False
         return
         # return
      #Apply Winner
      if (self.game_state == "BETTING_Showdown"):
         self.showdown()
         self.game_state = "reset_round"
         return
    
    def show_cards(self, player, blind):
      self.message_to_user =  blind + " Blind (" + player.player_id + "):" + self.show_player_hand(player) + "\n\nMake your bet!\n"

    def utg_bet(self, input):
      print(input)
      uinput = input
      #if player wants to leave, leave
      if(uinput == str(1)):
        self.message_to_user = self.get_utg() + " left the table, game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n" + self.get_winner()
        self.game_state = "leave"
        return
      #if player wants to fold, fold
      if(uinput == str(2)):
         self.utg.move = "Fold" #player move is 'Fold'
         self.second_better.money = self.second_better.money + self.pot # other player wins pot
         self.message_to_user = "\n\n" + str(self.get_utg()) + " folded, "\
         + str(self.get_second_bet()) + " wins the hand!\n"\
         + str(self.get_second_bet()) + " wins $" + str(self.pot) + "." #update message
         self.game_state = "reset_round" # update gamestate to 'reset_round'
         return
      #if player wants to check
      if(uinput == str(3)):
         #No money, all in!
         if (self.utg.money < self.bet):
            self.utg.move = "All-In" #player move is check
            self.pot = self.pot + self.utg.money # put all utg money in pot
            self.utg.money = 0 # update utg money to 0
            self.message_to_user = "\n\n" + str(self.get_utg()) + " is all in $" + str(self.bet) + "!\n" #update message
         else:
         #Normal check
            if(self.utg.money - self.bet > 0):
               self.utg.move = "Check" #player move is check
               self.pot = self.pot + self.bet  # update pot with the minimum bet
               self.utg.money = self.utg.money - self.bet #bet the minimum possible
               self.message_to_user =self.message_to_user+ "\n\n" + str(self.get_utg()) + " checked $" + str(self.bet) + ".\n" #update message
            else: #all in check
               self.utg.move = "All-In" #player move is check
               self.pot = self.pot + self.utg.money  # update pot all ur money
               self.utg.money = self.utg.money - self.bet #bet all ur money
               self.message_to_user = "\n\n" + str(self.get_utg()) + " is all in $" + str(self.bet) + "!\n" #update message
         if (self.second_better.move == "All-In"):#if 2nd is all in
            self.message_to_user = self.message_to_user + self.get_second_bet() + " is all in!\nShowdown begins!" #showdown
            self.game_state = "BETTING_Showdown"
         else:
            self.message_to_user = self.message_to_user + self.get_second_bet() + " bets next!\n"
            if(self.gamemode == "Human"):
               self.game_state = "BETTING_warn_show2nd_cards"
            else:
               self.game_state = "BETTING_show2nd_cards"
      #if player wants to bet
      if(uinput[:1] == str(4)):
         new_bet = int(uinput[2:]) #parse bet
         #if utg bet is < bet try again
         if (self.utg.money < new_bet):
            self.message_to_user = "\nYou cannot bet more than you have, try again."
            if(self.gamemode=="Human"):
               self.game_state = "BETTING_showUTG_cards"
            else:
               self.game_state = "BETTING_warn_showUTG_cards"
            return
         #elif utg money is == bet then techincally its a check
         elif (new_bet == self.bet):
            #No money, all in!
            if (self.utg.money < self.bet):
               self.utg.move = "All-In" #player move is check
               self.pot = self.pot + self.utg.money # put all utg money in pot
               self.utg.money = 0 # update utg money to 0
               self.message_to_user = "\n\n" + str(self.get_utg()) + " is all in $" + str(self.bet) + "!\n" #update message
            else:
            #Normal check
               if(self.utg.money - self.bet > 0):
                  self.utg.move = "Check" #player move is check
                  self.pot = self.pot + self.bet  # update pot with the minimum bet
                  self.utg.money = self.utg.money - self.bet #bet the minimum possible
                  self.message_to_user = "\n\n" + str(self.get_utg()) + " checked $" + str(self.bet) + ".\n" #update message
               else: #all in check
                  self.utg.move = "All-In" #player move is check
                  self.pot = self.pot + self.utg.money  # update pot all ur money
                  self.utg.money = self.utg.money - self.bet #bet all ur money
                  self.message_to_user = "\n\n" + str(self.get_utg()) + " is all in $" + str(self.bet) + "!\n" #update message
            if (self.second_better.move == "All-In"):#if 2nd is all in
               self.message_to_user = self.message_to_user + self.get_second_bet() + " is all in!\nShowdown begins!"#showdown
               self.game_state = "BETTING_Showdown"
            else:
               self.message_to_user = self.message_to_user + self.get_second_bet() + " bets next!\n"
               if(self.gamemode == "Human"):
                  self.game_state = "BETTING_warn_show2nd_cards"
               else:
                  self.game_state = "BETTING_show2nd_cards"
         #else bet like normal
         else:
            self.utg.move = 'Bet' #update move
            self.utg.money = self.utg.money - new_bet #subtract $ from player
            self.pot = self.pot + new_bet # add $ to pot
            self.bet = new_bet #update bet
            self.message_to_user = "\n" + self.get_utg() + " bet $" + str(new_bet) + ". " + self.get_second_bet() + " bets next!"
            if(self.gamemode == "Human"):
               self.game_state = "BETTING_warn_show2nd_cards"
            else:
               self.game_state = "BETTING_show2nd_cards"
         return

    def second_bet(self, uinput):
      #if player has no money, lose or all in 

      #if player wants to leave, leave
      if(uinput == str(1)):
        self.message_to_user = self.get_second_bet() + " left the table, game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n" + self.get_winner()
        self.game_state = "leave"
        return
      #if player wants to fold, fold
      if(uinput == str(2)):
         self.second_better.move = "Fold" #player move is 'Fold'
         self.second_better.money = self.utg.money + self.pot # utg wins pot
         self.message_to_user = "\n\n" + str(self.get_second_bet()) + " folded, "\
         + str(self.get_utg()) + " wins the hand!\n"\
         + str(self.get_utg()) + " wins $" + str(self.pot) #update message
         self.game_state = "reset_round" #gamestate to reset round
         return
      #if player wants to check
      if(uinput == str(3)):
         #if all in 
         if (self.second_better.money < self.bet):
            self.second_better.move = "All-In"
            self.pot = self.pot + self.second_better.money #update pot
            self.message_to_user = "\n\n" + str(self.get_second_bet()) + " is all in $" + str(self.second_better.money) + "\n"
            self.second_better.money = 0 #update money
            self.flop = self.flop + 1
         #regular check
         else:
            if(self.second_better.money - self.bet > 0):
               self.second_better.move = "Check"
               self.pot = self.pot + self.bet
               self.second_better.money = self.second_better.money - self.bet #update 2nd better money
               self.message_to_user = "\n\n" + str(self.get_second_bet()) + " checked $" + str(self.bet)+ ".\n"
               self.flop = self.flop + 1
            else: #after the check then 2nd better is all in
               self.second_better.move = "All-In"
               self.pot = self.pot + self.second_better.money
               self.message_to_user = "\n\n" + str(self.get_second_bet()) + " is all in $" + str(self.second_better.money) + "!\n"
               self.second_better.money = 0 #update 2nd better money
               self.flop = self.flop + 1
         #if utg is all in
         if (self.utg.move == "All-In"):
            self.game_state = "BETTING_Showdown" #Showdown
            self.message_to_user = "\n\n" + str(self.get_second_bet()) + " checked.\n" + self.get_utg() + " is all in!\nShowdown begins!\n"
         elif (self.flop == 4):
            self.game_state = "BETTING_Showdown" #Showdown
            self.message_to_user = "\n\n" + "Betting is over!\nShowdown begins!\n"
         #next flop
         else:
            self.message_to_user = self.message_to_user + self.get_utg() + " bets next!\n"\
                  + "\n\nMake your bet!"
            self.game_state = "BETTING_show_comm_cards_utg" #second better turn
      #if player wants to bet
      if(uinput == str(4)):
         if(self.utg.move == 'All-In'):
            #cannot raise when utg is already all in
            self.message_to_user = "\nCannot raise when " + self.get_utg()+ " is already all in"
            self.game_state = "BETTING_bet2nd"
            self.flop = self.flop + 1
            return
         else:
            #utg's turn again
            new_bet = int(uinput[2:]) #parse bet
            #TRYING TO BET MORE THAN YOU HAVE
            if (self.second_better.money < new_bet):
               self.game_state = "BETTING_bet2nd"
               self.message_to_user = "\nYou do not have that much money to bet Try again.\n"
            #ALL IN
            elif (self.second_better.money == new_bet): #all in
               self.second_better.move = 'All-In' #update move
               self.pot = self.pot + self.second_better.money # add $ to pot
               self.bet = new_bet # new bet is how much player put in
               self.message_to_user = "\n\n" + str(self.get_second_bet()) + " went all in $" + str(self.second_better.money) + "\n"\
                  + self.get_utg() + " bets next!\n"
               self.second_better.money = 0 #subtract $ from player
               self.flop = self.flop + 1
               self.game_state = "BETTING_show_comm_cards_utg"
            else: #normal bet
               self.second_better.move = 'Bet' #update move
               self.pot = self.pot + new_bet # add $ to pot
               self.second_better.money = self.second_better.money - new_bet #subtract $ from player
               self.bet = new_bet # new bet is how much player put in
               self.message_to_user = "\n\n" + str(self.get_second_bet()) + " bet" + str(new_bet) + "!\n"\
                  + self.get_utg() + " bets next!\n"
               self.flop = self.flop + 1
               self.game_state = "BETTING_show_comm_cards_utg" # round is not over so loop to get UTG to bet again