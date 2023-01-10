import pygame

from PGTE.pgte_engine import scenario_commands, personage


sc_1 = scenario_commands()
def scen_1_data_init():
    global sc_1
    sc_1 = scenario_commands()

    bs_sprites = {"cl_eye_smile":"data/images/sprites/bs/cl_eye_smile_1.png",
                  "concern":"data/images/sprites/bs/concern_1.png",
                  "norm":"data/images/sprites/bs/norm_1.png",
                  "one_eye_cl_smile":"data/images/sprites/bs/one_eye_cl_smile_1.png",
                  "shout":"data/images/sprites/bs/shout_1.png",
                  "sigh":"data/images/sprites/bs/sigh_1.png",
                  "sm_smile":"data/images/sprites/bs/sm_smile_1.png",
                  "unkindly":"data/images/sprites/bs/unkindly_1.png"}
    sc_1.pers_init("Босс", (215, 215, 215), "bs", bs_sprites)
    sc_1.init_music("data/music/vespercellos_all_go_to_plan.mp3", "vc_agtp")
    sc_1.pers_init("Я", (215, 215, 215), "i", {"none":"none"})
    sc_1.pers_init("", (213, 213, 213), "na", {"none":"none"}) # рассказчик/просто описание происходящего
    sc_1.init_bg("data/images/bg/office_building_2.png", "off_build_1")
    sc_1.init_bg("data/images/bg/office_3_day.png", "off_d_1")
    sc_1.init_bg("data/images/bg/office_1_evening.png", "off_ev_1")
    sc_1.init_bg("data/images/bg/office_1_night_off.png", "off_ni_off_1")
    sc_1.init_bg("data/images/bg/office_1_night_on.png", "off_ni_on_1")
    print(sc_1.personages["bs"].sprites)

def scenario_1():
    bsc_tuple = (450, 250)
    sc_1.tell("na", "09:30 по местному времени")
    sc_1.bg_img("off_build_1")
    sc_1.tell("na", 'Штаб квартира компании "Доставим быстро"')
    sc_1.tell("na", "...")
    sc_1.tell("i", "И это моё первое собеседование на роль грузчика")
    sc_1.play_music("vc_agtp")
    sc_1.bg_img()
    sc_1.tell("na", '"Untitled AS Studio" Представляет вашему вниманию:')
    sc_1.tell("na", 'Проект "Lame Future"')
    sc_1.tell("na", "...")
    sc_1.tell("na", "Когда вам надоест эта прекрасная музыка можете кликнуть чтобы продолжить")
    sc_1.stop_music()
    sc_1.tell("bs", "Итак")
    sc_1.bg_img("off_d_1")
    sc_1.show("bs", "unkindly", bsc_tuple[0], bsc_tuple[1])
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
    sc_1.tell("bs", "Очень надеюсь на это.")
    sc_1.tell("bs", "Ладно, начнем собеседование")
    sc_1.tell("bs", "Как ты относишься к возможным переработкам?")
    sc_1.tell("na", "Как же мне ответить?...")
    sc_1.tell("na", "От того что я сейчас скажу зависит моя работа")
    question = sc_1.choice("Спокойно", "Плохо", "Обажаю переработки!")
    bs = -2
    if(question == 1): # Спокойно
        sc_1.tell("i", "Я готов перерабатывать, если мне выплатят некоторую компенсацию")
        sc_1.tell("bs", "...")
        sc_1.tell("bs", "Ладно, сойдет")
    if(question == 2): # Плохо
        sc_1.tell("i", "Я ни за что не стану работать сверх нормы!")
        bs -= 1
        sc_1.show("bs", "sm_smile", bsc_tuple[0], bsc_tuple[1])
        sc_1.tell("bs", "Ну тогда я рад сообщить что ты уволен!")
        sc_1.hide()
        sc_1.bg_img()
        sc_1.tell("i", "Вот черт...")
        return
    if(question == 3): # Обажаю переработки!
        sc_1.tell("i", "Я всегда готов работать дополнительно на компанию!")
        bs += 1
        sc_1.show("bs", "sm_smile", bsc_tuple[0], bsc_tuple[1])
        sc_1.tell("bs", "Ладно, хоть что-то полезное в тебе есть")
        sc_1.tell("na", "~ Фух... Пронесло ~")
    sc_1.show("bs", "unkindly",  bsc_tuple[0], bsc_tuple[1])
    sc_1.tell("bs", "Следующий вопрос:")
    sc_1.tell("bs", "Какой у тебя опыт вождения грузовика?")
    question = sc_1.choice("Большой", "Средний", "Маленький")
    if(question == 1):
        sc_1.tell("i", "Я уже много лет вожу грузовики, в том числе и летающие")
        bs += 1
    if(question == 2):
        sc_1.tell("i", "Ну у меня есть некоторый опыт вождения грузовиков")
    if(question == 3):
        sc_1.tell("i", "Если честно я вообще почти грузовик не водил")
        bs -= 1

    if(bs < -2):
        sc_1.show("bs", "sm_smile", bsc_tuple[0], bsc_tuple[1])
        sc_1.tell("bs", "Ну что-же, тогда я рад сообщить что ты нам не подходишь")



    print(sc_1)