
#
# This class is the controller which might gatekeep to good inputs and directs to backend
#
class Controller(object):

    def __init__(self, game):
            self.game = game

    def start_game(self):
            self.game.start_game()
            return    
    
    def get_message_to_user(self):
            return self.game.get_message_to_user()
    
    def get_gamemode(self):
            return self.game.get_gamemode()
    
    def progress_game(self):
           return self.game.progress_game()

