import os
import sys

import pygame

from MakeButton import load_image
from configfile import screen

class scenario_commands():
    def __init__(self):
        self.sc_file = str()
        self.scenario = str()
        self.musics = dict()
        self.sounds = dict()
        self.backgrounds = dict()
        self.pfont = pygame.font.Font(None, 25)
        self.tfont = pygame.font.Font(None, 17)
        self.personages = dict()
        self.bg = str()

        # =============================================================================================================
        # Команды в файле сценария:
        #
        # play_music(music) - проигрывание фоновой музыки
        # stop_music() - остановить проигрыванние музыки
        # bg_img(file) - фоновое изображение
        # tell(pers, text) - Отобразить text сказанный персонажем pers
        # play_sound(file) - Проиграть звук
        # pers_init(name, color, sprites, cn) - Создать класс pers и объявить его имя в игре - name
        # Определить цвет имени в игре - color; Указать путь к папке со спрайтами - sprites; имя в сценарие - cn
        # hide(pers) - спрятать персонажа pers
        # show(pers) - показать персонажа pers
        # pers_pose(pers, file) - выбрать file с позой для персонажа pers
        # init_music(path, music) - путь path к музыке, music ключ для обращения в словарь с музыкой
        # init_sound(path, sound) - путь path к звуку, music ключ для обращения в словарь со звуками
        # init_bg(path, bg) - путь path к фону, bg ключ для обращения в словарь с фонами
        # =============================================================================================================
        # Условные знаки в тексте:
        #
        # ~p~ - пауза в диалоге
        # ~t~Text~t~ - Курсив
        # ~m~Text~m~ - Жирный шрифт

    def play_music(self, music):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self.musics[music])
            pygame.mixer.music.play(loops=-1)
        except:
            print(f"A music file named {music} was not found")

    def stop_music(self):
        pygame.mixer.music.stop()

    def init_music(self, path, music):
        self.musics[music] = path

    def init_sound(self, path, sound):
        self.sounds[sound] = path

    def play_sound(self, sound):
        try:
            pygame.mixer.init()
            s = pygame.mixer.Sound(self.sounds[sound])
            s.play()
        except:
            print(f"A sound file named {sound} was not found")

    def bg_img(self, bg):
        screen.blit(self.backgrounds[bg], (0, 0))
        self.bg = bg
        self.txt_bg = pygame.image.load("engine_imgs/txt_bg.png")
        screen.blit(self.txt_bg, (0, 638))


    def init_bg(self, path, bg):
        self.backgrounds[bg] = pygame.image.load(path)

    def tell(self, cn, text):
        self.bg_img(self.bg)
        personage_txt = self.pfont.render(self.personages[cn].name, True, self.personages[cn].color)
        screen.blit(personage_txt, (5, 645))
        text = self.tfont.render(text, True, (201, 201, 201))
        screen.blit(text, (5, 670))
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    running = False
    def show(self, pers):
        pass

    def hide(self, pers):
        pass

    def pers_init(self, name, color, sprites, cn):
        self.personages[cn] = personage(name, color, sprites, cn)

class personage():
    def __init__(self, name, color, sprites, cn):
        self.name = name
        self.color = color
        self.sprites_folder = sprites
        self.code_name = cn


if(__name__ == "__main__"):
    x = scenario_commands()
    x.init_music("../data/music/vespercellos_all_go_to_plan.mp3", "all_go_to_plan_1")
    print(x.musics)
    x.play_music("all_go_to_plan_1")
    x.init_sound("../data/sounds/dialog_click.mp3", "click_1")
    print(x.sounds)
    x.play_sound("click_1")
    pygame.init()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()