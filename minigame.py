import random
import sys

import pygame.image

from MakeButton import change_var, know_var
from configfile import screen, clock, FPS


class car():
    def __init__(self, sprite, speed, lane, xpos):
        self.sprite = sprite
        self.speed = speed
        self.lane = lane
        self.xpos = xpos
        self.iscolised = False

class race():
    def __init__(self):
        self.car_sprites = [pygame.image.load("data/minigame/2.png"),
                            pygame.image.load("data/minigame/3.png")]
        self.bg = pygame.image.load("data/minigame/bg.png")
        self.maincar = pygame.image.load("data/minigame/1.png")
        self.nomaincar = pygame.image.load("data/minigame/2.png")
        self.lanes = [80, 300, 520]
        self.mcl = 1
        self.cars = dict()

    def run(self, hard=5, finish=25):
        self.lifes = 3
        screen.blit(self.bg, (0, 0))
        lfont = pygame.font.SysFont("consolas", 59)
        self.running = True
        self.count = 0
        while(self.running and self.lifes > 0):
            screen.blit(self.bg, (0, 0))
            if(random.randint(1, 7*hard) == 1):
                self.new_car()
                self.count += 1
            self.main_car_move()
            self.bad_car_move()
            screen.blit(self.maincar, (950, self.lanes[self.mcl]))
            lifestxt = lfont.render(str(self.lifes), False, (255, 255, 255))
            screen.blit(lifestxt, (0, 0))
            clock.tick(60)
            pygame.display.flip()
        x = know_var("score")
        change_var("score", str(self.count + int(x)))

    def new_car(self):
        self.cars[self.count] = car(random.choice(self.car_sprites), 40,
                                    random.randint(0, 2), -280)

    def bad_car_move(self):
        try:
            for i in range(self.count + 1):
                screen.blit(self.cars[i].sprite, (self.cars[i].xpos, self.lanes[self.cars[i].lane]))
                self.cars[i].xpos += self.cars[i].speed
                if (self.iscollision(self.cars[i].xpos, self.cars[i].lane, 950, self.mcl)
                    and not self.cars[i].iscolised):
                    self.lifes -= 1
                    self.cars[i].iscolised = True
        except:
            pass

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

    def iscollision(self, car1x, car1l, car2x, car2l):
        if(car1l != car2l):
            return False
        distance = car1x - car2x
        if(-140 < distance < 350):
            return True


def level1():
    level = race()
    level.run(hard=3, finish=25)

def level2():
    level = race()
    level.run(hard=3, finish=25)

if(__name__ == "__main__"):
    change_var(name_of_var='score', new_value='0')
    level1()
    level2()
