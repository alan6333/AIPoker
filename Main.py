# Example file showing a circle moving on screen
import pygame, sys, time
import ptext
from Controller import Controller
from Backend import GameModel

class Button:
    def __init__(self, text, width, height, pos, type):
        #core attribs
        self.pressed = False
        self.type = type
        #top rectangle
        self.top_rect = pygame.Rect(pos, (width,height)) 
        self.top_color = "#CCE3DE"
        
        #text
        self.text_surf = gui_font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        #if hovering button
        if (self.top_rect.collidepoint(mouse_pos)):
            self.top_color = "#A4C3B2"
            #TODO change stuff here when hovering
            #status of mouse being clicked
            #if mouse is being clicked
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            #if player is not pressing button anymore (released)
            else:
                #if button was pressed in the first place
                self.top_color = "#6B9080"
                if (self.pressed == True):
                    if(self.type == "Gamemode"):
                        controller.choose_logistics("Human")
                        message = controller.get_message_to_user()
                        print(message)
                        controller.config_game()
                        message = controller.get_message_to_user()
                        print(message)
                        self.pressed == False

                    if(self.type == "Leave"):
                        controller.leave()
                        message = controller.get_message_to_user()
                        print(message)
                        return
                    if(self.type == "Betting"):
                        controller.betting(input)
                        message = controller.get_message_to_user()
                        print(message)
                        return

        #if mouse isn't hovering the button anymore
        else:
            self.top_color = "#CCE3DE"
            #TODO change button animation back when not hovering anymore
            return

def other_game_labels():
    #Flop
    flop = controller.get_flop()
    flopfont = pygame.font.Font(None, 64)
    text_surface = flopfont.render(flop, True, (255, 255, 255))
    ptext.draw(flop, (0, 750), color=pygame.Color('black'), background="white", fontsize=38)
    #Pot
    pot = "Pot: $"+ str(controller.get_pot())
    potfont = flopfont = pygame.font.Font(None, 64)
    ptext.draw(pot, (0, 780), color=pygame.Color('black'), background="white", fontsize=38)
    #Player $$$
    player1 = "Player 1: $"  + str(controller.get_player_money("p1"))
    playerfont = flopfont = pygame.font.Font(None, 64)
    ptext.draw(player1, (0, 500), color=pygame.Color('black'), background="white", fontsize=38)
    player2 = "Player 2: $"  + str(controller.get_player_money("p2"))
    ptext.draw(player2, (0, 530), color=pygame.Color('black'), background="white", fontsize=38)

def draw_comm_cards():
    card1 = pygame.image.load('./images/cards/spades/2-spades.PNG') #LOAD background
    card1 = pygame.transform.scale(card1, (400, 400)) #SCALE background
    screen.blit(bg, (350,400)) #places image onto screen

# PYGAME setup
pygame.init()
pygame.display.set_caption('AI Poker')
screen = pygame.display.set_mode((1280, 960), pygame.RESIZABLE) #1920x1080 or 3072x2304
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)
running = True
dt = 0
controller = Controller(GameModel())
#====================================================
is_game_started = False #has game started?
message = " " #message
bg = pygame.image.load('./images/bg-new.png') #LOAD background
bg = pygame.transform.scale(bg, (1280, 960)) #SCALE background
base_font = pygame.font.Font(None, 32)

all_buttons = []
all_buttons.append(Button('AI', 200, 60, (793,450), "Gamemode"))
all_buttons.append(Button('Human', 200, 60, (396,450), "Gamemode"))
all_buttons.append(Button('Leave', 200, 60, (0,0), "Leave"))
all_buttons.append(Button('Fold', 200, 60, (540,900), "Betting"))
all_buttons.append(Button('Check', 200, 60, (760,900), "Betting"))
# all_buttons.append(Button('Bet', 200, 60, (0,0), "Betting"))
#
#Main loop of the game
#if 'running' stops then the window closes.
#
while running:
    #place bg on screen
    screen.blit(bg, (0,0)) #places image onto screen

    text_surface = base_font.render(message, True, (255, 255, 255))
    ptext.draw(message, (0, 850), color=pygame.Color('black'), background="white")


    #PROGRESS GAME!
    if(controller.get_gamestate != "start" and controller.get_gamemode() != "N/A"):
        controller.progress_game()    
        message = controller.get_message_to_user()
        print(message)
        all_buttons[2].draw()
        all_buttons[3].draw()
        all_buttons[4].draw()

        #OTHER GAME LABELS
        other_game_labels()

    if(controller.if_awaiting_input()):
        print("awaiting input")

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #START GAME!
    if is_game_started == False:
        #1 ask for gamemode
        controller.ask_user_for_gamemode()
        message = controller.get_message_to_user()
        print(message)
        is_game_started = True
    #CHOOSE GAMEMODE
    if(controller.get_gamemode() == "N/A"):
        all_buttons[0].draw() #ai
        all_buttons[1].draw() #human

















    ##########################################################################################
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # dt = clock.tick(60) / 1000
    ##########################################################################################
pygame.quit()
