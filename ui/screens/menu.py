"""
This class displays the menu.

TODO: should display visual error if user tries to log into offline server (currently only prints a message in console).
"""
from ui.ui_objects import *
import pygame


DEBUG = False


#Button("CONNECT", "CONNECT", WINDOW_WIDTH / 2 + PADDING, WINDOW_HEIGHT / 2 - 50, GRAY, 0),
buttons = [Button("START", "START", WINDOW_WIDTH / 2 + PADDING - 90, WINDOW_HEIGHT / 2 + PADDING * 2 + 100, BLACK, 0)]


def draw(win):
    win.fill(WHITE)

    text = TITLE_FONT.render("Backgammon", 1, BLACK)
    win.blit(text, (round(WINDOW_WIDTH / 2) - round(text.get_width() / 2), 25))

    text = BODY_FONT_SMALL.render("v0.1", 1, BLACK)
    win.blit(text, (WINDOW_WIDTH - text.get_width() - PADDING, 150 - text.get_height() - PADDING))

    for b in buttons:
        b.draw(win)

    dices = pygame.image.load("ui/images/backgammon_ambiance3.png")
    win.blit(dices,(280,0))
    pygame.display.update()


def run(window, p1, p2):
    """
    :param window: window to draw on
    :param p1: player 1 (must be of type BackgammmonPlayer)
    :param p2: same as above
    :return: the next screen to transition to
    """
    if DEBUG:
        print("menu screen")

    display_screen = "MENU"
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in buttons:
                    if b.click(pos):
                        if b.button_id == "START":
                            return "INGAME", p1, p2, None
            # for t in text_boxes:
            #     t.handle_event(event)

        draw(window)
