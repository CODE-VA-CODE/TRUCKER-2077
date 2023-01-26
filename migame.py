import sys

import pygame.image

from configfile import screen, clock, FPS


class car():
    def __init__(self, sprite, speed, lane, xpos):
        self.sprite = sprite
        self.speed = speed
        self.lane = lane
        self.xpos = xpos

class race():
    def __init__(self):
        self.car_sprites = [pygame.image.load("data/minigame/2.png"),
                            pygame.image.load("data/minigame/3.png")]
        self.bg = pygame.image.load("data/minigame/bg.png")
        self.maincar = pygame.image.load("data/minigame/1.png")
        self.lanes = [80, 300, 520]
        self.mcl = 1
        self.cars = dict()

    def run(self, hard=5, finish=25):
        screen.blit(self.bg, (0, 0))
        self.running = True
        while(self.running):
            screen.blit(self.bg, (0, 0))
            screen.blit(self.maincar, (950, self.lanes[self.mcl]))
            self.main_car_move()
            clock.tick(60)
            pygame.display.flip()


    def main_car_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_UP):
                    self.mcl -= 1
                    if(self.mcl < 0):
                        self.mcl = 0
                if(event.key == pygame.K_DOWN):
                    self.mcl += 1
                    if(self.mcl > 2):
                        self.mcl = 2


x = race()
x.run()