import pygame

from PGTE.pgte_engine import scenario_commands, personage
from PGTE.scenarios.init_data import sc_1, scenario_init


def scen_1_data_init():
    bs_sprites = {"cl_eye_smile":"../data/images/sprites/bs/cl_eye_smile.png",
                  "concern":"../data/images/sprites/bs/concern.png",
                  "norm":"../data/images/sprites/bs/norm.png",
                  "one_eye_cl_smile":"../data/images/sprites/bs/one_eye_cl_smile.png",
                  "shout":"../data/images/sprites/bs/shout.png",
                  "sigh":"../data/images/sprites/bs/sigh.png",
                  "sm_smile":"../data/images/sprites/bs/sm_smile.png",
                  "unkindly":"../data/images/sprites/bs/unkindly.png"}
    sc_1.pers_init("Босс", (215, 215, 215), "bs", bs_sprites)
    sc_1.init_music("../data/music/vespercellos_all_go_to_plan.mp3", "vc_agtp")
    sc_1.pers_init("Я", (215, 215, 215), "i", ["pass"])
    sc_1.pers_init("", (213, 213, 213), "na", ["pass"]) # рассказчик/просто описание происходящего
    sc_1.init_bg("../data/images/bg/office_building_2.png", "off_build_1")
    sc_1.init_bg("../data/images/bg/office_3_day.png", "off_d_1")
    sc_1.init_bg("../data/images/bg/office_1_evening.png", "off_ev_1")
    sc_1.init_bg("../data/images/bg/office_1_night_off.png", "off_ni_off_1")
    sc_1.init_bg("../data/images/bg/office_1_night_on.png", "off_ni_on_1")
    print(sc_1.personages["bs"].sprites)

def scenario_1():
    sc_1.tell("na", "09:30 по местному времени")
    sc_1.bg_img("off_build_1")
    sc_1.tell("na", 'Штаб квартира компании "Доставим быстро"')
    sc_1.tell("na", "...")
    sc_1.tell("i", "И это моё первое собеседование на роль грузчика")
    sc_1.play_music("vc_agtp")
    sc_1.bg_img("black")
    sc_1.tell("na", '"Untitled AS Studio" Представляет вашему вниманию:')
    sc_1.tell("na", 'Проект "Lame Future"')
    sc_1.tell("na", "...")
    sc_1.tell("na", "Когда вам надоест эта прекрасная музыка можете кликнуть чтобы продолжить")
    sc_1.stop_music()
    sc_1.tell("bs", "Итак")
    sc_1.bg_img("off_d_1")
    sc_1.show("bs", "sm_smile")
    sc_1.tell("bs", "Не буду врать")
    sc_1.tell("bs", "Мне на тебя абсолютно наплевать")
    sc_1.tell("bs", "Я бы даже не стал нанимать тебя")
    sc_1.tell("bs", "Но от высшего руководства поступил запрос на то чтобы нанять ещё одного сотрудника")
    sc_1.tell("bs", "Так что запомни:")
    sc_1.tell("bs", "Тут с тобой никто нянчиться не будет")
    sc_1.tell("bs", "Лишь один промах с твоей стороны и я вышвырну тебя отсюда")
    sc_1.tell("na", "~Да уж, ну и отношение к новым сотрудникам~")
    sc_1.tell("na", "~Ладно, надо собраться, я же не тряпка~")
    sc_1.tell("i", "Так точно!")
    sc_1.tell("i", "Буду выполнять свою работу в лучшем виде!")
    sc_1.tell("bs", "Очень надеюсь на это")
    sc_1.tell("bs", "Ладно, тогда начнем собеседование")

    print(sc_1)