import pygame
from pygame.locals import *

from configfile import screen

pygame.init()
pygame.display.set_caption('End credits')
screen_r = screen.get_rect()
font = pygame.font.SysFont("Arial", 60)
clock = pygame.time.Clock()

def main():

    credit_list = ["LAME FUTURE"," "," ","Авторы идеи:","Зубов Семён", "Кириков Андрей", "и белый порошок :)", " ",
                   "Главный композитор:", "Андрэ", " ", "Главный Дизайнер:", "NemoSemi", " ",
                   "Ответственный за открытый мир:", "Zubov Semyon", " ", "Создатель движка PGTE:", "VA", " ",
                   "Главный редактор:", "Семен", " ", "Сценарист:", "Кириков А.", " ",
                   "Код в общем и целом:", "Untitled SA Studio", " ", " ", " ", " ", " ", " ", "Спасибо за внимание!"]

    texts = []
    for i, line in enumerate(credit_list):
        s = font.render(line, 1, (255, 255, 255))
        r = s.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 70)
        texts.append((r, s))
    pygame.mixer.init()
    pygame.mixer.music.load("data/music/vespercellos_all_go_to_plan_1.mp3")
    pygame.mixer.music.play()
    while True:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        screen.fill((0, 0, 0))

        for r, s in texts:
            print(s)
            r.move_ip(0, -1)
            screen.blit(s, r)

        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        pygame.display.flip()

        clock.tick(30)

if __name__ == '__main__':
    main()