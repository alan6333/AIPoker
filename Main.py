# Example file showing a circle moving on screen
import pygame
from Controller import Controller
from Backend import GameModel

# pygame setup
pygame.init()
pygame.display.set_caption('AI Poker')
screen = pygame.display.set_mode((1280, 720)) #1920x1080
clock = pygame.time.Clock()
running = True
dt = 0
controller = Controller(GameModel())
is_game_started = False
message = " "

#
#Main loop of the game
#if 'running' stops then the window closes.
#
while running:
    # poll for events
    # pygame.QUIT event means the user clickedç X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("brown")

    #start game
    if is_game_started == False:
        #1 ask for gamemode
        controller.ask_user_for_gamemode()
        message = controller.get_message_to_user()
        print(message)
        #2 answer to gamemode
        controller.choose_logistics()
        message = controller.get_message_to_user()
        print(message)
        #3 setup game logistics
        controller.config_game()
        message = controller.get_message_to_user()
        print(message)
        is_game_started = True

    controller.progress_game()    
    message = controller.get_message_to_user()
    print(message)
    

    ##########################################################################################
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    # dt = clock.tick(60) / 1000
    ##########################################################################################
pygame.quit()

