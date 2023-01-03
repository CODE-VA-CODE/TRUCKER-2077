import sys
import pygame
from MakeButton import load_image, MakeButton, know_var, change_var
from Options import OptionsGroup
from configfile import screen, clock, FPS


def continue_game(s):
    print('continue_game')


def exit(s):
    pygame.quit()
    sys.exit()


def play(s):
    print('play')


def options(s):
    while know_var('is_options'):
        for event in pygame.event.get():
            OptionsGroup.update(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(FPS)
    change_var('is_options', 'True')


class MainMenu(pygame.sprite.Sprite):
        main_image = load_image("MainMenu\MainMenu.png")
        logo_image = load_image("MainMenu\LameFuture470.png")

        def __init__(self, *group):
            super().__init__(*group)
            self.main_image = MainMenu.main_image
            self.logo_image = MainMenu.logo_image

        def update(self, *args):
            screen.blit(self.main_image, (0, 0))
            screen.blit(self.logo_image, (864, 184))


MainMenuButtonGroup = pygame.sprite.Group()
MainMenu = MainMenu()
ContinueButton = MakeButton(first_style="MainMenu\ContinueButton.png", first_style_background=-1, pos=[11, 11],
                            size=(500, 150), name_of_function=continue_game, arg_for_funtion=[], when_see=False)
PlayButton = MakeButton(first_style="MainMenu\PlayRus.png", first_style_background=-1, pos=[11, 171],
                        size=(500, 150), second_style="MainMenu\PlayRusSecond.png",  second_style_background=-1,
                        if_chage_style=True, name_of_function=play, arg_for_funtion=[])
OptionButton = MakeButton(first_style="MainMenu\OptionsRus.png", first_style_background=-1, pos=[11, 331],
                          size=(500, 150), second_style="MainMenu\OptionsRusSecond.png",  second_style_background=-1,
                          if_chage_style=True, name_of_function=options, arg_for_funtion=[])
ExitButton = MakeButton(first_style="MainMenu\ExitRus.png", first_style_background=-1, pos=[11, 491],
                        second_style="MainMenu\ExitRusSecond.png",  second_style_background=-1, size=(500, 150),
                        if_chage_style=True, name_of_function=exit, arg_for_funtion=[])
MainMenuButtonGroup.add(MainMenu, ContinueButton, PlayButton, OptionButton, ExitButton)
