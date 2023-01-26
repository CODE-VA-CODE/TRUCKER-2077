import sys

import pygame
from MakeButton import load_image, MakeButton, change_var, know_var, MusicPlayer, SysPlayer, SoundPlayer
from configfile import screen, clock, FPS
from credits import main


polz_value = {'music_vol': MusicPlayer,
              'sound_vol': SoundPlayer,
              'sys_vol': SysPlayer}


def go_back(s):
    change_var('is_options', 'False')


def chage_vol_state(name_of_val):
        change_var(name_of_var=name_of_val[0], new_value=name_of_val[1])
        if len(name_of_val) == 3:
            name_of_val[2].change_volume(name_of_val[1])

def autors(s):
    main()


#класс для создания ползунка
class MakePolz(pygame.sprite.Sprite):
    def __init__(self, *group, style, pos, size, name_vol):
        super().__init__(*group)
        # загружаем и преобразовываем изображение ползунка
        self.style = load_image(style)
        self.style = pygame.transform.scale(self.style, size)
        self.polz_rect = self.style.get_rect()
        self.polz_rect.x, self.polz_rect.y = pos
        # y - const, т.к. кусрор двигается только по оси х
        self.min_y = pos[1]
        #данная переменная нужна для определения конкретного показателя громкости в configefile.txt
        self.name_vol = name_vol
        #храним фактическую позицию ползунка, а отрисовываем по х - 15 (по середине курсора)
        #6.4 - константа для перевода координаты ползунка в громкость (от 1 до 100)
        self.pos = (int(know_var(self.name_vol)) * 6.4 + 260, self.min_y)
        self.go_polz = False #движение ползунка

    def update(self, *args):
        global polz_value
        self.pos = (int(know_var(self.name_vol)) * 6.4 + 260, self.min_y)
        # при отрисовке вычитаем 15 пикселей чтобы ползунок отрисовался по середине курсора по кординате х
        screen.blit(self.style, (self.pos[0] - 15, self.min_y))
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and \
                self.min_y <= args[0].pos[1] <= self.min_y + 50 and 260 <= args[0].pos[0] <= 900:
            self.go_polz = True
            #создаём группу спрайтов без заданого ползунка(его будет отрисовывать в цикле, а остальные спрайты статичны)
            MusicGroup = OptionsGroup.copy()
            if self.name_vol == 'music_vol':
                MusicGroup.remove(MusicPolz)
                SoundPolz.scr_blit()
                SysPolz.scr_blit()
            if self.name_vol == 'sound_vol':
                MusicGroup.remove(SoundPolz)
                MusicPolz.scr_blit()
                SysPolz.scr_blit()
            if self.name_vol == 'sys_vol':
                MusicGroup.remove(SysPolz)
                MusicPolz.scr_blit()
                SoundPolz.scr_blit()
            #необходимо отрисовать 2 оставшихся ползунка чтобы при зажатой левой кнопке мыши они были видны
            while self.go_polz:
                for event in pygame.event.get():
                    MusicGroup.update(event)
                    if event.type == pygame.MOUSEBUTTONUP or pygame.mouse.get_focused() == False:
                        self.go_polz = False
                    if pygame.mouse.get_focused():
                        if 260 <= event.pos[0] <= 900:
                            self.pos = (event.pos[0], self.polz_rect.y)
                            change_var(self.name_vol, int((int(self.pos[0]) - 250) // 6.4 - 1))
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    screen.blit(self.style, (self.pos[0] - 15, self.min_y))
                pygame.display.flip()
                clock.tick(FPS)
            polz_value[self.name_vol].change_volume(int(know_var(self.name_vol)))
            #640 пикселей - длина области с которой взаимодействует пользователь

    #отрисовывает ползунок без update
    def scr_blit(self):
        screen.blit(self.style, (self.pos[0] - 15, self.min_y))

class Options(pygame.sprite.Sprite):
        main_image = load_image("MainMenu\MainMenu.png")
        polz_image = load_image('MainMenu\Polzline.png', -1)

        def __init__(self, *group):
            super().__init__(*group)
            #шрифт, размер шрифта
            self.text_render_mode_1 = pygame.font.Font('data\shrift\Sprite.ttf', 110)
            self.text_render_mode_2 = pygame.font.Font('data\shrift\Sprite.ttf', 50)
            self.text_render_mode_3 = pygame.font.Font('data\shrift\Sprite.ttf', 30)
            #надпись, сглаживание, цвет
            self.text_settings = self.text_render_mode_1.render("Настройки", True, (255, 255, 255))
            self.text_music = self.text_render_mode_2.render("Музыка", True, (255, 255, 255))
            self.text_sound = self.text_render_mode_2.render("Звуки", True, (255, 255, 255))
            self.text_sys_1 = self.text_render_mode_3.render("Системные", True, (255, 255, 255))
            self.text_sys_2 = self.text_render_mode_3.render("Звуки", True, (255, 255, 255))
            self.main_image = Options.main_image
            self.polz_image = Options.polz_image
            self.polz_image = pygame.transform.scale(self.polz_image, (700, 50))

        def update(self, *args):
            screen.blit(self.main_image, (0, 0))
            screen.blit(self.text_settings, (440, 5))
            screen.blit(self.text_music, (50, 105))
            screen.blit(self.text_sound, (85, 180))
            screen.blit(self.text_sys_1, (60, 250))
            screen.blit(self.text_sys_2, (100, 275))
            screen.blit(self.polz_image, (233, 105))
            screen.blit(self.polz_image, (233, 180))
            screen.blit(self.polz_image, (233, 255))


Options = Options()
OptionsGroup = pygame.sprite.Group()
CircleMenuButton = MakeButton(first_style="MainMenu\OptionsCircle.png", first_style_background=-1, pos=[10, 10],
                              size=(75, 75), second_style="MainMenu\OptionsCircleSecond.png", if_chage_style=True,
                              second_style_background=-1, name_of_function=go_back, arg_for_funtion=[])
MusicVolButtonMin = MakeButton(first_style="MainMenu\MinRus.png", first_style_background=-1, pos=[940, 100],
                               size=(180, 60), second_style="MainMenu\MinRusSecond.png", if_chage_style=True,
                               second_style_background=-1, name_of_function=chage_vol_state,
                               arg_for_funtion=['music_vol', 0, MusicPlayer])
MusicVolButtonMax = MakeButton(first_style="MainMenu\MaxRus.png", first_style_background=-1, pos=[1127, 100],
                               size=(180, 60), second_style="MainMenu\MaxRusSecond.png", if_chage_style=True,
                               second_style_background=-1, name_of_function=chage_vol_state,
                               arg_for_funtion=['music_vol', 100, MusicPlayer])
SoundVolButtonMin = MakeButton(first_style="MainMenu\MinRus.png", first_style_background=-1, pos=[940, 175],
                               size=(180, 60), second_style="MainMenu\MinRusSecond.png",  second_style_background=-1,
                               name_of_function=chage_vol_state, arg_for_funtion=['sound_vol', 0],
                               if_chage_style=True)
SoundVolButtonMax = MakeButton(first_style="MainMenu\MaxRus.png", first_style_background=-1, pos=[1127, 175],
                               size=(180, 60), second_style="MainMenu\MaxRusSecond.png",  second_style_background=-1,
                               name_of_function=chage_vol_state, arg_for_funtion=['sound_vol', 100],
                               if_chage_style=True)
SysVolButtonMin = MakeButton(first_style="MainMenu\MinRus.png", first_style_background=-1, pos=[940, 250],
                             size=(180, 60), second_style="MainMenu\MinRusSecond.png",  second_style_background=-1,
                             name_of_function=chage_vol_state, arg_for_funtion=['sys_vol', 0], if_chage_style=True)
SysVolButtonMax = MakeButton(first_style="MainMenu\MaxRus.png", first_style_background=-1, pos=[1127, 250],
                             size=(180, 60), second_style="MainMenu\MaxRusSecond.png",  second_style_background=-1,
                             name_of_function=chage_vol_state, arg_for_funtion=['sys_vol', 100], if_chage_style=True)
Autors = MakeButton(first_style="MainMenu\Autors.png", first_style_background=-1, pos=[578, 678],
                    size=(210, 70), second_style="MainMenu\AutorsSecond.png",  second_style_background=-1,
                    name_of_function=autors, arg_for_funtion=[None], if_chage_style=True)
MusicPolz = MakePolz(style='MainMenu\Polz.png', pos=[335, 105], size=(30, 50), name_vol='music_vol')
SoundPolz = MakePolz(style='MainMenu\Polz.png', pos=[335, 180], size=(30, 50), name_vol='sound_vol')
SysPolz = MakePolz(style='MainMenu\Polz.png', pos=[335, 255], size=(30, 50), name_vol='sys_vol')
OptionsGroup.add(Options, CircleMenuButton, MusicVolButtonMin, MusicVolButtonMax, SoundVolButtonMin, SoundVolButtonMax,
                 SysVolButtonMin, SysVolButtonMax, Autors, MusicPolz, SoundPolz, SysPolz)
