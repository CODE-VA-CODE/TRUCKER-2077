import pygame
from pygame.locals import *

from configfile import screen, clock
from MakeButton import MusicPlayer, know_var

pygame.init()
pygame.display.set_caption('End credits')
screen_r = screen.get_rect()
print(screen_r, screen_r.centerx, screen_r.bottom, sep="\n")
font = pygame.font.SysFont("Arial", 60)

def main():

    credit_list = ["LAME FUTURE"," "," ","Авторы идеи:","Зубов Семён", "Кириков Андрей", " ",
                   "Главный композитор:", "Андрей (Который спер все из инета)", "", "Главный Дизайнер:", "NemoSemi", "",
                   "Ответственный за открытый мир:", "Zubov Semyon", " ", "Создатель движка PGTE:", "VA", " ",
                   "Главный редактор:", "Семен", " ", "Сценарист:", "Кириков А.", " ",
                   "В игре использовались треки групп:", "Гражданская оборона", "Vespercellos", " ",
                   "Фоны и спрайты были взяты", "с бесплатных ресурсов интернета", "так как рисовать мы не умеем)", "",
                   "Код в общем и целом:", "Untitled SA Studio", " ", " ", " ", " ", " ", " ", "Спасибо за внимание!"]

    texts = []
    for i, line in enumerate(credit_list):
        cred_str = font.render(line, 1, (255, 255, 255))
        rend_str = cred_str.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 70)
        texts.append((rend_str, cred_str))
    MusicPlayer.music_load("data/music/vespercellos_all_go_to_plan_1.mp3")
    MusicPlayer.music_play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
                MusicPlayer.music_stop()
                return

        screen.fill((0, 0, 0))

        for rend_str, prev_str in texts:
            rend_str.move_ip(0, -1)
            screen.blit(prev_str, rend_str)

        if not screen_r.collidelistall([r for (r, _) in texts]):
            MusicPlayer.music_stop()
            return

        pygame.display.flip()

        clock.tick(30) # ОБЯЗАТЕЛЬНО УСТАНОВИТЬ 30 ПЕРЕД РЕЛИЗОМ

if __name__ == '__main__':
    main()