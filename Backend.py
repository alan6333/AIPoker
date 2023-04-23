from GameHelperFunctions import make_card_deck, shuffle_card_deck
import GameHelperFunctions
import time, random

class Card:
  def __init__(self, suit, number, value):
    self.suit = suit
    self.number = number
    self.value = value

  def printCard(self):
    print(self.suit + " " + self.number)
  
class Player:
   def __init__(self):
      self.money = 2900
      self.blind = "Undecided"
      self.cards = [0,0]

class GameModel():
    def __init__(self):
       self.gamemode = "AI" # default vs AI
       self.game_state = "start" 
       self.utg = "Undecided"
       self.second_better = "Undecided"
       self.p1 = Player()
       self.p2 = Player()
       self.message_to_user = "Welcome to AI Poker by Alan Coronado"
       self.card_deck = []

    def start_game(self):
        #change game state
        self.game_state = "ask_user_for_gamemode"
        #make and actually shuffle cards ahaha
        self.card_deck = make_card_deck(self.card_deck)
        self.card_deck = shuffle_card_deck(self.card_deck)
        time.sleep(1)
        #set message to user
        self.message_to_user = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"\
          "Welcome to AI Poker by Alan Coronado\nThe dealer is shuffling cards...\n"
        time.sleep(1)
        return
    
    
    def progress_game(self):
      if self.game_state == 'ask_user_for_gamemode':
          self.ask_user_for_gamemode()
      
      elif self.game_state == "choose_logistics":
          self.choose_logistics()

      elif self.game_state[0:8] == "pre_flop": #prefix 'preflop', if gamestate is preflop phase
          self.pre_flop()
          return
      
      elif self.game_state == " ":
        print(" ")

      elif self.game_state == "leave":
          self.leave()
      
      else:
          print("\n\n\nI'm not done yet! QUIT.")
          quit()
      return 
        
        
    def get_message_to_user(self):
      return self.message_to_user
    
    def get_gamemode(self):
      return self.gamemode 
    
    def choose_blinds(self):
      randomNum = random.randrange(2)
      if (randomNum == 0):
         self.p1.blind = "Small"
         self.utg = self.p1
         self.p2.blind = "Big"
         self.second_better = self.p2
      else:
         self.p1.blind = "Big"
         self.second_better = self.p1
         self.p2.blind = "Small"
         self.utg = self.p2
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
    
#======================================================================================================================
    def leave(self):
       quit()

    def ask_user_for_gamemode(self):
        self.message_to_user = "Please choose your opponent, type 'AI' or 'Human': "
        self.game_state = "choose_logistics"
        return
    
    def choose_logistics(self):

      #set little and big blinds
      self.choose_blinds()

      #give 2 cards to each player
      self.deal_2_cards(self.p1)
      self.deal_2_cards(self.p2)

      uinput = input()
      if (uinput == "AI"):
          self.message_to_user = "Ready to play against: AI!\n\nThe Dealer is done Shuffling\n\n"\
          + "Big Blind is " + str(self.get_big_blind()) + " and Small Blind is " + str(self.get_small_blind())\
          + "\nThe dealer is handing out cards!\n\n\n\n----==={Pre-Flop Begin}===----\n\n"
          self.gamemode = "AI"
          self.game_state = "pre_flop"
      elif (uinput == "Human"):
          self.message_to_user = "\nReady to play against: AI!\n\nThe Dealer is done shuffling.\n\n"\
          + "Big Blind is " + str(self.get_big_blind()) + " and Small Blind is " + str(self.get_small_blind())\
          + "\nThe dealer is handing out cards!\n\n\n\n----==={Pre-Flop Begin}===----\n\n"
          self.gamemode = "Human"
          self.game_state = "pre_flop"
      else:
          self.message_to_user = "\nInvalid input, try again.\nPlease a VALID opponent, type 'AI' or 'Human': "      
      return
    

    def pre_flop(self):

      if (self.game_state == "pre_flop"):
          self.message_to_user = str(self.get_small_blind()) + " is Under The Gun with $" + str(self.get_player_money(self.utg)) +" dollars.\n" + "Make your bet!\n"\
          + "Options: 1[Leave] 2[Fold] 2[Check] 3[Bet (amount)]"
          self.game_state = "pre_flop_utg_bet"
      elif (self.game_state == "pre_flop_utg_bet"):
         self.player_bet(self.utg)

    
    def player_bet(self, player):
      
      uinput = input()
      #if player has no money, lose
      #if player wants to leave, leave
      if(uinput == str(1)):
        self.message_to_user = "\n\n\n\n=======================================================================================\n"\
            + self.get_utg() + " left the table, game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
         + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n" + self.get_winner()
        self.game_state = "leave"
      #if player wants to fold, fold
      #if player wants to bet
