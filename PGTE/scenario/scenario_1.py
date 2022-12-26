import pygame

from PGTE.pgte_engine import scenario_commands, personage
from PGTE.scenario.init_data import sc_1, scenario_init


def scenario_1():
    scenario_init()
    sc_1.bg_img("bg_1")
    sc_1.tell("sm", "HELLO!!!")
    sc_1.tell("sm", "sawhrfaf!")
    choice = sc_1.choice("1", "2")
    if(choice == 1):
        sc_1.tell("sm", "1")
    if(choice == 2):
        sc_1.tell("sm", "2")

    print(sc_1)