from ui import ui_constants
from ui.screens import menu, ingame
import pygame
import sys
from agents import SkeletonAgent, backgammon_ssbg

player1 = backgammon_ssbg.BackgammonPlayer()
player2 = SkeletonAgent.BackgammonPlayer()

DETERMINISTIC = False  # deterministic version: dice are loaded to give 1 and 6
# stochastic version (DETERMINISTIC = false): dice are rolled normally.

# Student's UW net-id
username = "user"

# DO NOT CHANGE ANY CODE BELOW THIS
# ------------------------------------------------------------------------------------------------------------------
pygame.init()
pygame.display.init()
pygame.display.set_caption("Backgammon")
window = pygame.display.set_mode((ui_constants.WINDOW_WIDTH, ui_constants.WINDOW_HEIGHT))
DEBUG = False

try:
    sys.path.append('~/ui')
    sys.path.append('~/server')
    sys.path.append('~/game_engine')
    sys.path.append('~/agents')
    print("Updated path - Backgammon GUI is ready to use.")
except:
    print("ERROR: ui, server, game_engine, or agents folder is missing. Could not update path")

def start_client():
    next_screen = menu.run(window, player1, player2)

    while True:
        if DEBUG:
            print(next_screen)
        if next_screen == "QUIT":
            pygame.quit()
            exit()
        elif next_screen == "MENU":
            next_screen = menu.run(window, player1, player2)
        elif len(next_screen) > 1 and next_screen[0] == "INGAME":
            p1 = next_screen[1]
            p2 = next_screen[2]
            computed_game = next_screen[3]
            print(type(p1))
            print(type(p2))
            if p1 is not None:
                if p2 is not None:
                    next_screen = ingame.run(window, p1, p2, DETERMINISTIC, computed_game)
                else:
                    raise Exception("player2 should not be None")
            else:
                raise Exception("player1 should not be None")
        else:
            raise Exception("Invalid game state transition.")


start_client()
