from GameHelperFunctions import make_card_deck, shuffle_card_deck
import GameHelperFunctions
import time, random

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
      self.player_id = id

#
# This class is the backend, keeps track of the game logic
#
class GameModel():
    def __init__(self):
       self.gamemode = "AI" # default vs AI
       self.game_state = "start" 
       self.pot = 0 #pot of money
       self.utg = "Undecided" #UTG means the player next to the dealer, they always start the bet
       self.second_better = "Undecided" #only 2 player so there is only one other better
       self.p1 = Player("Player 1") 
       self.p2 = Player("Player 2")
       self.message_to_user = "Welcome to AI Poker by Alan Coronado" # this var is what the frontend uses to print
       self.card_deck = [] 

    #game config method
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
    
    #important method to flow the game state
    #Will need to alter this method into some sort of a loop to account for continuous betting
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
       
    def show_player_hand(self, player):
      return "Your cards are: \n" + player.cards[0].number + "-" +  player.cards[0].suit + " " + player.cards[1].number + "-" +  player.cards[1].suit
    
    def blinds_bet(self):
       p1_bet = 0
       p2_bet = 0
       #p1 is Big blind
       if (self.p1=="Big"):
          p1_bet = 50
          p2_bet = 25
       else: #p1 is small blind
          p1_bet = 25
          p2_bet = 50
       #P1 and P2 have no money
       if (self.p1.money < p1_bet and self.p2.money < p2_bet):
          self.message_to_user += "Player 1 & p2 have no money" \
          + "\n\n\n\n=======================================================================================\n"\
            + "Its a tie, the game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n" + self.get_winner()
          self.game_state = "leave"
       #P1 has no money
       elif (self.p1.money < p1_bet and self.p2.money >= p2_bet):
          self.message_to_user += "Player 1 has no money" \
          + "\n\n\n\n=======================================================================================\n"\
            + "Player 2 wins! The game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n" + self.get_winner()
          self.game_state = "leave"
       #P2 has no money
       elif (self.p1.money >= p1_bet and self.p2.money < p2_bet):
          self.message_to_user += "Player 2 has no money" \
          + "\n\n\n\n=======================================================================================\n"\
            + "Player 1 wins! The game is over.\n" + "Player 1 earnings: $" + str(self.get_player_money(self.p1))\
            + "\nPlayer 2 earnings: $" + str(self.get_player_money(self.p2)) + "\n" + self.get_winner()
          self.game_state = "leave"
       #everyone has money, do the bets
       else:
          self.message_to_user = "Player 1 is " + self.p1.blind + " blind & bet $" + str(p1_bet) + "!\n"\
          "Player 2 is " + self.p2.blind + " blind & bet $" + str(p2_bet) + "!"
          self.p1.money = self.p1.money - p1_bet
          self.p2.money = self.p2.money - p2_bet
          self.pot = self.pot + p1_bet + p2_bet
   
    def switch_blinds(self):
         #switch blinds for next round
          if (self.p1.blind == "Small"):
             self.p1.blind = "Big"
             self.p2.blind = "Small"
          else:
             self.p1.blind = "Small"
             self.p2.blind = "Big"

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
          self.message_to_user = "Ready to play against: AI!\n\nThe Dealer is done Shuffling\n"\
          + "\n\n\n\n----==={Pre-Flop Begin}===----\n"
          self.gamemode = "AI"
          self.game_state = "pre_flop_blindbet"
      elif (uinput == "Human"):
          self.message_to_user = "\nReady to play against: AI!\n\nThe Dealer is done shuffling.\n"\
          + "\n\n\n\n----==={Pre-Flop Begin}===----\n"
          self.gamemode = "Human"
          self.game_state = "pre_flop_blindbet"
      else:
          self.message_to_user = "\nInvalid input, try again.\nPlease a VALID opponent, type 'AI' or 'Human': "      
      return
    

    def pre_flop(self):

      if (self.game_state == "pre_flop_blindbet"):
         self.blinds_bet()
         self.game_state = "pre_flop"
      elif (self.game_state == "pre_flop"):
         self.message_to_user = "\n" + str(self.get_small_blind()) + " is 'Under The Gun' with $" + str(self.get_player_money(self.utg)) +" dollars.\n"\
          + "Showing " + self.utg.player_id + " cards in 5 seconds.\n\n\n"
         self.game_state = "pre_flop_showcards_5sec_cool"
      elif (self.game_state == "pre_flop_showcards_5sec_cool"):
         self.message_to_user = " "
         self.game_state = "pre_flop_showcards"
         time.sleep(5)
      elif (self.game_state == "pre_flop_showcards"):
         self.show_cards()
      elif (self.game_state == "pre_flop_utg_bet"):
         self.player_bet(self.utg)

    
    def show_cards(self):
      self.message_to_user =  self.show_player_hand(self.utg) + "\n\nMake your bet!\n"\
          + "Options: 1[Leave] 2[Fold] 2[Check] 3[Bet (amount)]\n"
      self.game_state = "pre_flop_utg_bet"

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
