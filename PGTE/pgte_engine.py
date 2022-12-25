# engine file for Py Game Tell Engine
import pygame


class scenario_commands():
    def __init__(self):
        self.sc_file = str()
        self.scenario = str()
        # =============================================================================================================
        # Команды в файле сценария:
        #
        # play_music(file) - проигрывание фоновой музыки
        # bg_img(file) - фоновое изображение
        # tell(pers, text) - Отобразить text сказанный персонажем pers
        # play_sound(file) - Проиграть звук
        # pers_init(name, color, sprites, cn) - Создать класс pers и объявить его имя в игре - name
        # Определить цвет имени в игре - color; Указать путь к папке со спрайтами - sprites; имя в сценарие - cn
        # hide(pers) - спрятать персонажа pers
        # show(pers) - показать персонажа pers
        # pers_pose(pers, file) - выбрать file с позой для персонажа pers
        # =============================================================================================================
        # Условные знаки в тексте:
        #
        # ~p~ - пауза в диалоге
        # ~t~Text~t~ - Курсив
        # ~m~Text~m~ - Жирный шрифт

    def open_scenario(self, sc_file):
        self.sc_file = sc_file
        with open(self.sc_file, encoding="utf-8") as sc:
            self.scenario = sc.read().splitlines()
        if(__name__ == "__main__"):
            print(self.scenario)

    def scenario_run(self):
        line_number = 0
        for line in self.scenario:
            line_number += 1
            if(line[:2] == "pl"):
                if(line[5] == "m"):
                    self.play_music(line[11:-1])
                elif (line[5] == "s"):
                    self.play_sound(line[11:-1])

            elif(line[:2] == "bg"):
                self.bg_img(line[11:-1])

            elif(line[:2] == "te"):
                self.tell(line[11:-1])

            elif(line[:2] == "pe"):
                self.pers_init(line[11:-1])

            elif(line[:2] == "hi"):
                self.hide(line[11:-1])

            elif(line[:2] == "sh"):
                self.show(line[11:-1])

    def play_music(self, music):
        pass

    def play_sound(self, sound):
        pass

    def bg_img(self, bg):
        pass

    def tell(self, pers, text):
        pass

    def pers_init(self, name, color, sprites, cn):
        pass

    def show(self, pers):
        pass

    def hide(self, pers):
        pass

class personage():
    def __init__(self, name, color, sprites, cn):
        self.name = name
        self.color = color
        self.sprites_folder = sprites
        self.code_name = cn


if(__name__ == "__main__"):
    scenario_commands().open_scenario("scenario\scenario.txt")
if(__name__ == "__main__"):
    print("OK")