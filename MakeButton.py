import pygame
import os, sys
from configfile import screen


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class MakeButton(pygame.sprite.Sprite):
    def __init__(self, *group, first_style, first_style_background=None, pos, size=None,
                 second_style=None, second_style_background=None, if_chage_style=False, when_see=True,
                 name_of_function, arg_for_funtion):
        #переменные first_style и first_style_background отвечают за инициализацию базовой картинки
        #переменные pos и size отвечают за позицию и размер кнопки соответственно
        #переменные second_style, second_style_background и if_chage_style являются необязательными отвечают за смену
        #дизайна кнопки при наведении мышкой наведении на неё курсора мыши
        #переменная when_see отвечает за условие при котором кнопка будет видна
        #name_of_function и arg_for_funtion отвечают за имя функции и параметры которые будут ей передаваться
        super().__init__(*group)
        self.first_style = load_image(first_style, first_style_background)
        if second_style != None:
            self.second_style = load_image(second_style, second_style_background)
        if size != None:
            self.first_style = pygame.transform.scale(self.first_style, size)
        self.function = name_of_function
        self.arg_for_function = arg_for_funtion
        self.button_rect = self.first_style.get_rect()
        self.copy_of_first_style = self.first_style
        self.button_rect.x, self.button_rect.y = pos
        self.pos = pos
        self.when_see = when_see
        self.if_chage_style = if_chage_style

    def update(self, *args):
        if self.when_see:
            screen.blit(self.first_style, self.pos)
        if self.if_chage_style and self.button_rect.collidepoint(args[0].pos):
            self.first_style = self.second_style
        if self.if_chage_style and self.button_rect.collidepoint(args[0].pos) == False:
            self.first_style = self.copy_of_first_style
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.button_rect.collidepoint(args[0].pos) and self.when_see:
            self.function(self.arg_for_function)
