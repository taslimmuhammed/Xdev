from pygame.locals import *
import os
from settings import * 
import sys
import pygame as pg


pg.init()

class Window:

    def __init__(self):
        # self.m1 = Game(0)
        self.screen = pg.display.set_mode((screen_width, screen_height))
        self.rect = self.screen.get_rect()
        self.FPS = 30
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 25)
        self.menu_open = True
        self.colors = {"red": (255, 0, 0),
                       "green": (0, 255, 0),
                       "blue": (0, 0, 255),
                       "white": (255, 255, 255),
                       "black": (0, 0, 0),
                       "brown": (153, 76, 0),
                       "grey": (100, 100, 100)}

    def setup(self):
        self.screen.fill(self.colors["black"])
        pg.display.set_caption("Menu Test!")

    def text(self, message, text_color, x_pos, y_pos):
        text = self.font.render(message, True, (self.colors[text_color]))
        text_rect = text.get_rect(center=(x_pos, y_pos))
        self.screen.blit(text, text_rect)

    def exit(self):
        self.screen.fill(self.colors["black"])
        text = self.font.render("Thank you for playing. Goodbye from xDev!", True,
                                (self.colors["white"]))
        text_rect = text.get_rect(center=(self.rect.w/2, self.rect.h/2))
        self.screen.blit(text, text_rect)
        pg.display.update()
        pg.time.wait(1000)
        pg.quit()
        sys.exit()


class Button(pg.sprite.Sprite):

    def __init__(self, pos, text, window):
        super().__init__()  # Call __init__ of the parent class.
        # Render the text.
        self.text_surf = window.font.render(text, True, window.colors["black"])
        self.image = pg.Surface((self.text_surf.get_width()+40,
                                 self.text_surf.get_height()+20))
        self.image.fill(window.colors["white"])
        # Now blit the text onto the self.image.
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)


def main():
    window = Window()
    window.setup()
    clock = pg.time.Clock()
    # gui is a sprite group which will contain the button sprites.
    gui = pg.sprite.Group()
    # Instantiate some buttons.
    quit_button = Button(
        pos=(window.rect.w/2 - 100, window.rect.h/1.5 - 25),
        text="QUIT",
        window=window,
        )
    hello_button = Button(
        pos=(window.rect.w/8, window.rect.h/2),
        text="START",
        window=window,
        )
    # Add the buttons to the gui group.
    gui.add(quit_button, hello_button)

    while window.menu_open == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                window.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                # Handle button events.
                if quit_button.rect.collidepoint(event.pos):
                    window.exit()
                elif hello_button.rect.collidepoint(event.pos):
                    print("hello")
                    from main import Game
                    # m1.run()


        gui.update()  # Call update methods of contained sprites.
        gui.draw(window.screen)  # Draw all sprites.
        pg.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()