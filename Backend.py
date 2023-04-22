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

      elif self.game_state == "Round 0":
          self.round0()
          return

      elif self.game_state == " ":
          print(" ")
      
      else:
          print("I'm not done yet! QUIT.")
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
         self.utg = "P1"
         self.p2.blind = "Big"
      else:
         self.p1.blind = "Big"
         self.p2.blind = "Small"
         self.utg = "P2"
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
       
    
#======================================================================================================================
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
          + "\nThe dealer is handing out cards!"
          self.gamemode = "AI"
          self.game_state = "Round0"
      elif (uinput == "Human"):
          self.message_to_user = "\nReady to play against: AI!\n\nThe Dealer is done shuffling.\n\n"\
          + "Big Blind is " + str(self.get_big_blind()) + " and Small Blind is " + str(self.get_small_blind())\
          + "\nThe dealer is handing out cards!"
          self.gamemode = "Human"
          self.game_state = "Round0"
      else:
          self.message_to_user = "\nInvalid input, try again.\nPlease a VALID opponent, type 'AI' or 'Human': "      
      return
    


    # def round0player(self):
      # choose blinds, small is "under the gun" UTG

      # UTG bets first
      # big blind goes second
      # chance to leave



