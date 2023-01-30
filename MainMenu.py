import sys
import pygame
from MakeButton import load_image, MakeButton, know_var, change_var
from Options import OptionsGroup
from PGTE.run import run
from PGTE.scenarios.final_dialog_with_boss import start_final_dialog_with_boss
from PGTE.scenarios.first_order_finish import finish_first_order
from PGTE.scenarios.second_order_finish import finish_second_order
from PGTE.scenarios.second_order_start import start_second_order
from configfile import screen, clock, FPS
from PGTE.scenarios.first_order_start import start_first_order
from credits import main, final_scores
from minigame import level2, level1


def exit(s):
    pygame.quit()
    sys.exit()


def play(s):
    change_var(name_of_var='interview_stat', new_value='True')
    change_var(name_of_var='score', new_value='0')
    if know_var('continue') == False:
        start_second_order()
        level2()
        finish_second_order()
        start_final_dialog_with_boss()  # 1
        main()
    if int(know_var('number_of_lvl')) == 1 and know_var('continue'):
        run()
        if know_var('interview_stat'):
            start_first_order()
            level1()
            finish_first_order()
    if int(know_var('number_of_lvl')) == 2 and know_var('continue'):
        start_second_order()
        level2()
        finish_second_order()
        start_final_dialog_with_boss()
        main()
        final_scores()
    change_var(name_of_var='continue', new_value='True')

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
PlayButton = MakeButton(first_style="MainMenu\PlayRus.png", first_style_background=-1, pos=[11, 171],
                        size=(500, 150), second_style="MainMenu\PlayRusSecond.png",  second_style_background=-1,
                        if_chage_style=True, name_of_function=play, arg_for_funtion=[])
OptionButton = MakeButton(first_style="MainMenu\OptionsRus.png", first_style_background=-1, pos=[11, 331],
                          size=(500, 150), second_style="MainMenu\OptionsRusSecond.png",  second_style_background=-1,
                          if_chage_style=True, name_of_function=options, arg_for_funtion=[])
ExitButton = MakeButton(first_style="MainMenu\ExitRus.png", first_style_background=-1, pos=[11, 491],
                        second_style="MainMenu\ExitRusSecond.png",  second_style_background=-1, size=(500, 150),
                        if_chage_style=True, name_of_function=exit, arg_for_funtion=[])
MainMenuButtonGroup.add(MainMenu, PlayButton, OptionButton, ExitButton)
