import pygame

from PGTE.pgte_engine import scenario_commands, personage

sc_1 = scenario_commands()

def scenario_init():
    sc_1.init_music("../data/music/vespercellos_all_go_to_plan.mp3", "all_go_to_plan_1")
    sc_1.init_bg("../data/images/one1.png", "bg_1")
    print(sc_1.backgrounds)
    sc_1.init_sound("../data/sounds/dialog_click.mp3", "click_1")
    sc_1.pers_init("Семен", (170, 255, 255), 1, "sm")
    print(sc_1.personages)