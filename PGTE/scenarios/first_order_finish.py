import pygame

from MakeButton import MusicPlayer, change_var
from PGTE.pgte_engine import scenario_commands


def first_order_finish_init():
    global first_ord_fin
    first_ord_fin = scenario_commands()
    first_ord_sprites = {'farmer_with': 'data/images/sprites/first_order/farmer_with.png',
                         'farmer_without': 'data/images/sprites/first_order/farmer_without.png'}
    first_ord_fin.pers_init("Рабочий", (215, 215, 215), "farmer", first_ord_sprites)
    first_ord_fin.init_music("data/music/Shiro Sagisu - Cruel Dilemme III", "farmer_music")
    first_ord_fin.pers_init("Я", (215, 215, 215), "i", {"none":"none"})
    first_ord_fin.pers_init("", (213, 213, 213), "na", {"none":"none"}) # рассказчик/просто описание происходящего
    first_ord_fin.init_bg("data/images/bg/roof.png", "roof_bg")


def first_order_finish():
    bsc_tuple = (300, 237)
    first_ord_fin.tell("i", "Наконец-то я доехал, дорога была такой утомительной")
    first_ord_fin.bg_img("roof_bg")
    MusicPlayer.music_load('data/music/quitemusic.mp3')
    first_ord_fin.show("farmer", "farmer_with", bsc_tuple[0], bsc_tuple[1])
    MusicPlayer.music_play()
    first_ord_fin.tell("na", "~ Нужно скорее найти начальника и сбагрить ему этот груз ~")
    first_ord_fin.tell('na', '~ ... ~')
    first_ord_fin.tell('na', '~ А вот кажется и он ~')
    first_ord_fin.tell("i", "Здравствуйте, я грузчик из фирмы 'Доставим быстро', вот ваш заказ")
    first_ord_fin.tell("farmer", "Так, давайка посмотрим чо ты там привёз...")
    first_ord_fin.bg_img()
    first_ord_fin.hide()
    first_ord_fin.tell('na', '~ осматривает прицеп ~')
    first_ord_fin.bg_img("roof_bg")
    first_ord_fin.show("farmer", "farmer_without", 300, 222)
    first_ord_fin.tell("farmer", "Ну, вроде всё на месте и цело")
    first_ord_fin.tell("farmer", "Спасибо за доставку, вы можете быть свободны")
    first_ord_fin.tell("i", "Нет проблем, были рабы посотрудничать в вашей компанией")
    first_ord_fin.bg_img()
    first_ord_fin.hide()
    MusicPlayer.music_stop()
    first_ord_fin.tell('na', '~ вы возвращаетесь к боссу и получаете новый заказ ~')
    question = first_ord_fin.choice("Продолжить", "Выйти в главное меню")
    if(question == 1):
        change_var(name_of_var='number_of_lvl', new_value='2')
    else:
        change_var(name_of_var='number_of_lvl', new_value='2')
        change_var(name_of_var='continue', new_value='False')


def finish_first_order():
    first_order_finish_init()
    first_order_finish()
    pygame.display.flip()

if(__name__ == "__main__"):
    finish_first_order()
