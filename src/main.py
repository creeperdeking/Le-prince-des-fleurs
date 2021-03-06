import pygame
from Intro.intro import *
from Controllers.MenuController import MenuController

def main():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    gameDisplay = pygame.display.set_mode((1024,768))
    pygame.display.set_caption('Le Prince Des Fleurs')
    launchIntro(gameDisplay)
    menuController = MenuController(gameDisplay)

main()
pygame.quit()
quit()
