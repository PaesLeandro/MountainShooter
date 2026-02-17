import pygame

from Code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from Code.level import Level
from Code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Mountain Shooter")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window,  'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # Fecha a janela
                quit() # Encerra o jogo
            else:
                pass

