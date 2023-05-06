
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
        
        def betting(self, input):
                self.game.betting(input)
                return
        
        def leave(self):
                self.game.leave()
                return