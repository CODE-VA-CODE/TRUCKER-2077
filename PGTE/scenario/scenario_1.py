import pygame

from PGTE.pgte_engine import scenario_commands, personage
from PGTE.scenario.init_data import sc_1, scenario_init


def scenario_1():
    scenario_init()
    sc_1.bg_img("bg_1")
    sc_1.tell("sm", "HELLO!!!")
    sc_1.play_music("all_go_to_plan_1")
    sc_1.tell("sm", "safasfaf!")
    print(sc_1)