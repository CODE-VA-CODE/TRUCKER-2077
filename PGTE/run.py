import pygame

from PGTE.pgte_engine import scenario_commands
from PGTE.scenarios.interview_1 import scenario_1, scen_1_data_init


def run():
    scen_1_data_init()
    scenario_1()
    pygame.display.flip()

if(__name__ == "__main__"):
    run()