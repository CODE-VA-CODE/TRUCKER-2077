import pygame
from MakeButton import load_image, MakeButton, change_var, MakePolz
from configfile import screen


def go_back(s):
    change_var('is_options', 'False')


def chage_vol_state(name_of_val):
        change_var(name_of_var=name_of_val[0], new_value=name_of_val[1])


class Options(pygame.sprite.Sprite):
        main_image = load_image("MainMenu\MainMenu.png")
        polz_image = load_image('MainMenu\Polzline.png', -1)

        def __init__(self, *group):
            super().__init__(*group)
            #шрифт, размер шрифта
            self.text_render_mode_1 = pygame.font.Font('data\shrift\Sprite.ttf', 110)
            self.text_render_mode_2 = pygame.font.Font('data\shrift\Sprite.ttf', 50)
            self.text_render_mode_3 = pygame.font.Font('data\shrift\Sprite.ttf', 30)
            #найдись, сглаживание, цвет
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
                               arg_for_funtion=['music_vol', 0])
MusicVolButtonMax = MakeButton(first_style="MainMenu\MaxRus.png", first_style_background=-1, pos=[1127, 100],
                               size=(180, 60), second_style="MainMenu\MaxRusSecond.png", if_chage_style=True,
                               second_style_background=-1, name_of_function=chage_vol_state,
                               arg_for_funtion=['music_vol', 100])
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
MusicPolz = MakePolz(style='MainMenu\Polz.png', pos=[335, 105], size=(30, 50), name_vol='music_vol')
SoundPolz = MakePolz(style='MainMenu\Polz.png', pos=[335, 180], size=(30, 50), name_vol='sound_vol')
SysPolz = MakePolz(style='MainMenu\Polz.png', pos=[335, 255], size=(30, 50), name_vol='sys_vol')
OptionsGroup.add(Options, CircleMenuButton, MusicVolButtonMin, MusicVolButtonMax, SoundVolButtonMin, SoundVolButtonMax,
                 SysVolButtonMin, SysVolButtonMax, MusicPolz, SoundPolz, SysPolz)
