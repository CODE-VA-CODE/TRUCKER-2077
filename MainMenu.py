import sys
import pygame
from MakeButton import load_image, MakeButton
from configfile import screen


def continue_game(s):
    print('continue_game')


def exit(s):
    pygame.quit()
    sys.exit()


def play(s):
    print('play')


def options(s):
    print('options')


class MainMenu(pygame.sprite.Sprite):
        main_image = load_image("MainMenu\MainMenu.png")
        logo_image = load_image("MainMenu\LameFutureText.png", -1)


        def __init__(self, *group):
            super().__init__(*group)
            self.main_image = MainMenu.main_image
            self.rect = self.main_image.get_rect()
            self.rect.x, self.rect.y = 0, 0

            self.logo_image = MainMenu.logo_image
            self.rectf = self.main_image.get_rect()
            self.rectf.x, self.rectf.y = 0, 0

        def update(self, *args):
            screen.blit(self.main_image, (0, 0))
            screen.blit(self.logo_image, (0, 0))


MainMenuButtonGroup = pygame.sprite.Group()
MainMenu = MainMenu()
ContinueButton = MakeButton(first_style="MainMenu\ContinueButton.png", first_style_background=-1, pos=[433, 158],
                            size=(500, 150), name_of_function=continue_game, arg_for_funtion=[1, 'sdf'], when_see=True)
PlayButton = MakeButton(first_style="MainMenu\PlayButton.png", first_style_background=-1, pos=[433, 308],
                            size=(500, 150), name_of_function=play, arg_for_funtion=[1, 'sdf'])
OptionButton = MakeButton(first_style="MainMenu\OptionsButton.png", first_style_background=-1, pos=[433, 458],
                            size=(500, 150), name_of_function=options, arg_for_funtion=[1, 'sdf'])
ExitButton = MakeButton(first_style="MainMenu\ExitButton.png", first_style_background=-1, pos=[433, 608],
                            size=(500, 150), name_of_function=exit, arg_for_funtion=[1, 'sdf'])
MainMenuButtonGroup.add(MainMenu, ContinueButton, PlayButton, OptionButton, ExitButton)
