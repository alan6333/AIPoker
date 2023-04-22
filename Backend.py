from GameHelperFunctions import make_card_deck, shuffle_card_deck
import GameHelperFunctions
import time

class card:
  def __init__(self, suit, number, value):
    self.suit = suit
    self.number = number
    self.value = value

  def printCard(self):
    print(self.suit + " " + self.number)

class GameModel():

    def __init__(self):
       self.gamemode = "1Player"
       self.game_state = "start" #start, input_game_type, 
       self.big_blind = "Undecided"
       self.p1_chips = 2900
       self.p2_chips = 2900
       self.message_to_user = "Welcome to AI Poker by Alan Coronado"
       self.card_deck = []

    def start_game(self):
        #change game state
        self.game_state = "ask_for_gamemode"
        #make and actually shuffle cards ahaha
        self.card_deck = make_card_deck(self.card_deck)
        self.card_deck = shuffle_card_deck(self.card_deck)
        time.sleep(1)
        #set message to user
        self.message_to_user = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"\
          "Welcome to AI Poker by Alan Coronado\nThe dealer is shuffling cards...\n"
        time.sleep(1)
        return

    def choose_gamemode(self):
      uinput = input()
      if (uinput == "AI"):
          self.message_to_user = "Ready to play against: AI!\nThe Dealer is done Shuffling\n"
          self.gamemode = "AI"
          self.game_state = "Round0"
          return
      elif (uinput == "Human"):
          self.message_to_user = "Ready to play against: AI!\nThe Dealer is done Shuffling\n"
          self.gamemode = "Human"
          self.game_state = "Round0"
          return
      else:
          self.message_to_user = "\nInvalid input, try again.\nPlease a VALID opponent, type 'AI' or 'Human': "
          return
    
    def progress_game(self):
      if self.game_state == 'ask_for_gamemode':
          self.message_to_user = "Please choose your opponent, type 'AI' or 'Human': "
          self.game_state = "receive_gamemode"
          return
      
      elif self.game_state == "receive_gamemode":
          self.choose_gamemode()

      elif self.game_state == "Round 0":
          self.round0()
          return

      elif self.game_state == " ":
          print(" ")
      
      else:
          print("I'm , QUIT")
          quit()

      return 
        
        
    def get_message_to_user(self):
      return self.message_to_user
    
    def get_gamemode(self):
      return self.gamemode 
    
    # def round0player(self):
      # choose blinds, small is "under the gun" UTG

      # UTG bets first
      # big blind goes second
      # chance to leave



