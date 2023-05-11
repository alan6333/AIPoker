# Example file showing a circle moving on screen
import pygame, sys, time, pygame_gui
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
        self.top_color = "#4F695E"
        
        #text
        self.text_surf = gui_font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color, self.top_rect)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        global bet_button
        mouse_pos = pygame.mouse.get_pos()
        #if hovering button
        if (self.top_rect.collidepoint(mouse_pos)):
            self.top_color = "#35463F"
            #TODO change stuff here when hovering
            #status of mouse being clicked
            #if mouse is being clicked
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            #if player is not pressing button anymore (released)
            else:
                #if button was pressed in the first place
                self.top_color = "#35463F"
                if (self.pressed == True):
                    if(self.type == "Human" or self.type=="AI"):
                        if(self.type == "Human"):
                            controller.choose_logistics("Human")
                        else:
                            controller.choose_logistics("AI")
                        message = controller.get_message_to_user()
                        print(message)
                        controller.config_game()
                        message = controller.get_message_to_user()
                        print(message)
                    
                    #1 Leave, 2 Fold, 3 Check, 4 Bet
                    if(self.type == "1" or self.type == "2" or self.type == "3"):
                        controller.input_bet(self.type)
                        message = controller.get_message_to_user()
                        print(message)
                        controller.set_awaiting_input(False)
                    if(self.type == "4"):
                        if(bet_button == False):
                            TEXT_INPUT.enable()
                            bet_button = True
                        else:
                            TEXT_INPUT.disable()
                            bet_button = False

                    self.pressed = False

        #if mouse isn't hovering the button anymore
        else:
            self.top_color = "#4F695E"
            #TODO change button animation back when not hovering anymore
            return

def other_game_labels():
    #Flop
    flop = controller.get_flop()
    flopfont = pygame.font.Font("Milenia.ttf", 64)
    text_surface = flopfont.render(flop, True, (255, 255, 255))
    ptext.draw(flop, (0, 650), color=pygame.Color('black'), background="white", fontsize=24, fontname="Milenia.ttf")
    #Pot
    pot = "Pot: $"+ str(controller.get_pot())
    potfont = pygame.font.Font("Milenia.ttf", 64)
    ptext.draw(pot, (0, 600), color=pygame.Color('black'), background="white", fontsize=24, fontname="Milenia.ttf")
    #Player $$$
    player1 = "Player 1: $"  + str(controller.get_player_money("p1"))
    playerfont = flopfont = pygame.font.Font("Milenia.ttf", 64)
    ptext.draw(player1, (0, 400), color=pygame.Color('black'), background="white", fontsize=24, fontname="Milenia.ttf")
    player2 = "Player 2: $"  + str(controller.get_player_money("p2"))
    ptext.draw(player2, (0, 450), color=pygame.Color('black'),fontname="Milenia.ttf", background="white", fontsize=24)

def draw_comm_cards():
    card1 = pygame.image.load('./images/cards/spades/2-spades.PNG') #LOAD background
    card1 = pygame.transform.scale(card1, (400, 400)) #SCALE background
    screen.blit(bg, (350,400)) #places image onto screen

# PYGAME setup
pygame.init()
pygame.display.set_caption('AI Poker')
global bet_button
global progress_game
MANAGER = pygame_gui.UIManager((1280, 960))
TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((1180,900),(100,60)), manager=MANAGER, object_id="#main_text_entry")
screen = pygame.display.set_mode((1280, 960), pygame.RESIZABLE, ) #1920x1080 or 3072x2304
clock = pygame.time.Clock()
gui_font = pygame.font.Font("Milenia.ttf", 30)
running = True
dt = 0
controller = Controller(GameModel())
#====================================================
is_game_started = False #has game started?
message = " " #message
bg = pygame.image.load('./images/bg-new.png') #LOAD background
bg = pygame.transform.scale(bg, (1280, 960)) #SCALE background
base_font = pygame.font.Font("Milenia.ttf", 32)
bet_button = False
progress_game = False
all_buttons = []
all_buttons.append(Button('AI', 200, 60, (793,450), "AI"))
all_buttons.append(Button('Human', 200, 60, (396,450), "Human"))
all_buttons.append(Button('Leave', 200, 60, (0,0), "1"))
all_buttons.append(Button('Fold', 200, 60, (540,900), "2"))
all_buttons.append(Button('Check', 200, 60, (760,900), "3"))
all_buttons.append(Button('Bet', 200, 60, (980,900), "4"))
all_buttons.append(Button('->', 200, 30, (673,900), "progress_game"))
#
#Main loop of the game
#if 'running' stops then the window closes.
#
while running:
    print(controller.get_gamestate())
    #place bg on screen
    screen.blit(bg, (0,0)) #places image onto screen

    #PROGRESS GAME! and controller.if_awaiting_input() == False
    if(controller.get_gamestate() != "start" and controller.get_gamemode() != "N/A"):
        # if (controller.get_gamestate() == "quit"):
            # pygame.time.wait(5000)
        controller.progress_game()    
        message = controller.get_message_to_user()
        all_buttons[2].draw()
        all_buttons[3].draw()
        all_buttons[4].draw()
        all_buttons[5].draw()
        #OTHER GAME LABELS
        other_game_labels()
        if ("BETTING_bet" != controller.get_gamestate()[:11] and "BETTING" == controller.get_gamestate()[:7]):
            pygame.time.wait(10000)

    #IF WAITING FOR INPUT, WAIT
    # if(controller.if_awaiting_input() == True):
    #     all_buttons[2].draw()
    #     all_buttons[3].draw()
    #     all_buttons[4].draw()
    #     print("awaiting input")
    #     #OTHER GAME LABELS
    #     other_game_labels()




    # pygame.QUIT event means the user clicked X to close your window
    UI_REFRESH_RATE = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry"):
            controller.input_bet("4 " + str(event.text))
            message = controller.get_message_to_user()
            print(message)
            controller.set_awaiting_input(False)

        MANAGER.process_events(event)
    MANAGER.update(UI_REFRESH_RATE)
    if(bet_button == True):
        MANAGER.draw_ui(screen)
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

    #write to message box
    text_surface = base_font.render(message, True, (255, 255, 255))
    ptext.draw(message, (0, 750), color=pygame.Color('black'), background="white", fontname="Milenia.ttf", fontsize=24)

















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
