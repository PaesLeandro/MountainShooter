import pygame
from Code.Const import WIN_HEIGHT, WIN_WIDTH
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
            menu.run()
            pass

