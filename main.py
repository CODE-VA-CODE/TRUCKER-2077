import sys
import pygame
from MainMenu import MainMenuButtonGroup
from configfile import clock, FPS


while True:
    for event in pygame.event.get():
        MainMenuButtonGroup.update(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(FPS)
