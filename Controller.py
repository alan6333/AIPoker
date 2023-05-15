
#
# This class is the controller which might gatekeep to good inputs and directs to backend
#
class Controller(object):

        def __init__(self, game):
                self.game = game

        def ask_user_for_gamemode(self):
                return self.game.ask_user_for_gamemode()
        
        def choose_logistics(self, uinput):
                return self.game.choose_logistics(uinput)

        def config_game(self):
                self.game.config_game()
                return    
        
        def get_message_to_user(self):
                return self.game.get_message_to_user()
        
        def get_gamemode(self):
                return self.game.get_gamemode()
        
        def progress_game(self):
                return self.game.progress_game()

        def get_gamestate(self):
                return self.game.get_gamestate()

        def if_awaiting_input(self):
                return self.game.if_awaiting_input()
        
        def set_awaiting_input(self, bool):
                return self.game.set_awaiting_input(bool)
        
        def betting(self, input):
                self.game.betting(input)
                return
        
        def input_bet(self, input):
                self.game.input_bet(input)
                return
        
        def leave(self):
                self.game.leave()
                return
        
        def get_flop(self):
                return self.game.get_flop()
        
        def get_pot(self):
                return self.game.get_pot()
        
        def get_player_money(self, player):
                return self.game.get_player_cash(player)
        
        def get_second_better_move(self):
                return self.game.get_second_better_move()
        
        def show_comm_cards(self):
                return self.game.show_comm_cards()

        def get_player_id(self, player):
                return self.game.get_player_id(player)