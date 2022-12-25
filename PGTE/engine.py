# engine file for Py Game Tell Engine
import pygame


class scenario_commands():
    def __init__(self):
        pass
        # =============================================================================================================
        # Команды в файле сценария:
        #
        # play_music(file) - проигрывание фоновой музыки
        # bg_img(file) - фоновое изображение
        # tell(pers, text) - Отобразить text сказанный персонажем pers
        # play_sound(file) - Проиграть звук
        # pers_init(name, color, sprites, cn) - Создать класс pers и объявить его имя в игре - name
        # Определить цвет имени в игре - color; Указать путь к папке со спрайтами - sprites; имя в сценарие - cn
        # hide(pers) спрятать персонажа pers
        # show(pers) показать персонажа pers
        # =============================================================================================================
        # Условные знаки в тексте:
        #
        # ~p~ - пауза в диалоге
        # ~t~Text~t~ - Курсив
        # ~m~Text~m~ - Жирный шрифт

    def read_scenario(self, sc_file):
        self.sc_file = sc_file
        with open(self.sc_file, encoding="utf-8") as sc:
            self.text = sc.read()

        return(self.text)


if(__name__ == "__main__"):
    print("OK")