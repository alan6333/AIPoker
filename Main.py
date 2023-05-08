# Example file showing a circle moving on screen
import pygame, sys
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
        self.top_color = "#475F77"
        
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
            #TODO change stuff here when hovering
            #status of mouse being clicked
            #if mouse is being clicked
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            #if player is not pressing button anymore (released)
            else:
                #if button was pressed in the first place
                if (self.pressed == True):
                    if(self.type == "Gamemode"):
                        controller.choose_logistics("Human")
                        message = controller.get_message_to_user()
                        print(message)
                        #TODO might have to put a wait here
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
            #TODO change button animation back when not hovering anymore
            return

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# PYGAME setup
pygame.init()
def box_text(surface, font, x_start, x_end, y_start, text, colour):
    x = x_start
    y = y_start
    words = text.split(' ')

    for word in words:
        word_t = font.render(word, True, colour)
        if word_t.get_width() + x <= x_end:
            surface.blit(word_t, (x, y))
            x += word_t.get_width() * 1.1
        else:
            y += word_t.get_height() * 1.1
            x = x_start
            surface.blit(word_t, (x, y))
            x += word_t.get_width() * 1.1
pygame.display.set_caption('AI Poker')
screen = pygame.display.set_mode((1280, 960)) #1920x1080 or 3072x2304
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)
running = True
dt = 0
controller = Controller(GameModel())
#====================================================
is_game_started = False #has game started?
message = " " #message
bg = pygame.image.load('./images/bg.jpg') #LOAD background
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
    # screen.blit(text_surface, (210,0))
    # blit_text(text_surface, message, (210, 0), pygame.font.SysFont('Arial', 64))
    ptext.draw(message, (0, 850), color=pygame.Color('black'), background="white")
    # pygame.QUIT event means the user clickedç X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #start game
    if is_game_started == False:
        #1 ask for gamemode
        controller.ask_user_for_gamemode()
        message = controller.get_message_to_user()
        print(message)
        is_game_started = True
    #if gamemode isn't choosen yet
    if(controller.get_gamemode() == "N/A"):
        all_buttons[0].draw() #ai
        all_buttons[1].draw() #human
    #if game has started progress game
    if(controller.get_gamestate != "start" and controller.get_gamemode() != "N/A"):
        controller.progress_game()    
        message = controller.get_message_to_user()
        print(message)
        all_buttons[2].draw()
        all_buttons[3].draw()
        all_buttons[4].draw()
    if(controller.if_awaiting_input()):
        print("awaiting input")
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
