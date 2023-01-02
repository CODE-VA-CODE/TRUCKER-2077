import pygame
import os, sys

from configfile import screen, clock, FPS


#функция для подгрузки изображений
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


#класс для создания кнопок
class MakeButton(pygame.sprite.Sprite):
    def __init__(self, *group, first_style, first_style_background=None, pos, size=None,
                 second_style=None, second_style_background=None, if_chage_style=False,
                 when_see=True, name_of_function, arg_for_funtion):
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
                self.second_style = pygame.transform.scale(self.second_style, size)
        if size != None:
            self.first_style = pygame.transform.scale(self.first_style, size)
        self.copy_style = self.first_style
        self.function = name_of_function
        self.arg_for_function = arg_for_funtion
        self.button_rect = self.first_style.get_rect()
        self.button_rect.x, self.button_rect.y = pos
        self.pos = pos
        self.when_see = when_see
        self.if_chage_style = if_chage_style

    def update(self, *args):
        if self.when_see:
            screen.blit(self.first_style, self.pos)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.button_rect.collidepoint(args[0].pos) and self.when_see:
            if self.if_chage_style:
                screen.blit(self.second_style, self.pos)
            self.function(self.arg_for_function)

    def hide(self):
        self.when_see = False

    def scr_blit(self):
        screen.blit(self.first_style, self.pos)

#функция для изменения содержимого конфиг файла
def change_var(name_of_var, new_value):
    with open('configefile.txt', mode='r') as f:
        file = f.readlines()
        new_file = file
        for string in file:
            strok = string.replace('\n', '').split()
            if strok[0] == name_of_var:
                new_file[file.index(string)] = f'{name_of_var} = {new_value}\n'
                break
        with open('configefile.txt', mode='w') as save:
            for i in new_file:
                save.write(i)


#функция для возврата значения переменной из конфиг файла
def know_var(name_of_var):
    with open('configefile.txt', mode='r') as f:
        file = f.readlines()
        for string in file:
            #храним строки из конфиг файла в виде ['имя переменной', '=', 'значение переменной']
            strok = string.replace('\n', '').split()
            if strok[0] == name_of_var:
                if strok[-1] == 'True':
                    return True
                if strok[-1] == 'False':
                    return False
                else:
                    return strok[-1]
