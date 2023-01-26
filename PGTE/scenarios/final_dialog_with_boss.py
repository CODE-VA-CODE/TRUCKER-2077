import pygame

from MakeButton import change_var
from PGTE.pgte_engine import scenario_commands, personage


def final_dialog_data_init():
    global sc_1
    sc_1 = scenario_commands()

    bs_sprites = {"one_eye_cl_smile":"data/images/sprites/bs/one_eye_cl_smile_1.png",
                  "unkindly":"data/images/sprites/bs/unkindly_1.png"}
    sc_1.pers_init("Босс", (215, 215, 215), "bs", bs_sprites)
    sc_1.pers_init("Я", (215, 215, 215), "i", {"none":"none"})
    sc_1.pers_init("", (213, 213, 213), "na", {"none":"none"}) # рассказчик/просто описание происходящего
    sc_1.init_bg("data/images/bg/office_3_day.png", "off_d_1")
    sc_1.init_bg("data/images/bg/office_building_2.png", "off_build_1")

def final_dialog():
    bsc_tuple = (450, 250)
    sc_1.bg_img("off_build_1")
    sc_1.tell("i", "Пора узнать ответы на вопросы")
    sc_1.bg_img("off_d_1")
    sc_1.show("bs", "unkindly", bsc_tuple[0], bsc_tuple[1])
    sc_1.tell("bs", "...")
    sc_1.tell("bs", "Ну и зачем ты пришёл сюда, я же выслал тебе новый заказ?")
    sc_1.tell("i", "Босс, у меня есть парочку вопросов к вам...")
    sc_1.tell("bs", "...")
    sc_1.tell("bs", "Если твои вопросы не удивят меня то ты сегодня же будешь уволен")
    question = sc_1.choice("Рассказать про строителя", "Рассказать про странный товар")
    if(question == 1):
        sc_1.tell("i", "Вчера я доставлял заказ со стройки и мне показалось что один из их сотрудников очень странный")
        sc_1.tell("bs", "Что такого он сделал?")
        sc_1.tell("i", "Он перепутал меня с доставщиком еды")
        sc_1.tell("bs", "Просто не обращай внимания, строители они все такие")
        sc_1.tell("bs", "И это всё?!")
        sc_1.tell("i", "Нет...")
        sc_1.tell("i", "Во время последней доставки мне отказались говорить что находится внутри груза, а это нарушает правила компании")
    if(question == 2):
        sc_1.tell("i", "Во время последней доставки мне отказались говорить что находится внутри груза, а это нарушает правила компании")
    sc_1.show("bs", "one_eye_cl_smile", bsc_tuple[0], bsc_tuple[1])
    sc_1.tell("bs", "Пф...")
    sc_1.tell("i", 'Что такое?')
    sc_1.tell("bs", "...")
    sc_1.tell("bs", "Ты до сих пор не догадался что на простых посылках наша компания далеко бы не уехала?")
    sc_1.tell("i", 'Что вы имеете в виду?')
    sc_1.tell("bs", "Наша компания прикрывает всех контробандистов в городе")
    sc_1.tell("bs", 'Именно поэтому мы так сильно разраслись всего за полтора года')
    sc_1.show("bs", "unkindly", bsc_tuple[0], bsc_tuple[1])
    sc_1.tell("bs", "...")
    sc_1.tell("bs", "Теперь когда ты знаешь правду у тебя остаётся всего 2 варианта...")
    sc_1.tell("bs", "Первый, самый благоприятный для нас обоих - ты примкнешь к нам")
    sc_1.tell("bs", "А второй...")
    sc_1.tell("bs", "Думаю ты сам понимаешь о чём я")
    sc_1.tell("na", "~ Как же мне быть ~")
    question = sc_1.choice("Примкнуть", "Отказаться")
    sc_1.tell("i", 'Босс, я выбираю...')
    sc_1.bg_img()
    sc_1.hide()
    sc_1.tell("na", "Продолжение следует")
    change_var(name_of_var='number_of_lvl', new_value='1')

def start_final_dialog_with_boss():
    final_dialog_data_init()
    final_dialog()
    pygame.display.flip()

if(__name__ == "__main__"):
    start_final_dialog_with_boss()