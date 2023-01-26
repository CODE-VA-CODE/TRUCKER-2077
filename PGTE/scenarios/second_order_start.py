import pygame

from MakeButton import MusicPlayer
from PGTE.pgte_engine import scenario_commands


def second_order_start_init():
    global second_ord
    second_ord = scenario_commands()
    second_ord_sprites = {'agronom_normal': 'data/images/sprites/second_order/agronom_normal.png'}
    second_ord.pers_init("Агроном", (215, 215, 215), "agronom", second_ord_sprites)
    second_ord.init_music("data/music/Shiro Sagisu - Cruel Dilemme III", "farmer_music")
    second_ord.pers_init("Я", (215, 215, 215), "i", {"none":"none"})
    second_ord.pers_init("", (213, 213, 213), "na", {"none":"none"}) # рассказчик/просто описание происходящего
    second_ord.init_bg("data/images/bg/farm.png", "farm_bg")

def second_order_start():
    bsc_tuple = (450, 250)
    second_ord.bg_img("farm_bg")
    MusicPlayer.music_load('data/music/quitemusic.mp3')
    second_ord.tell("i", "Так, а вот и место из второго заказа")
    MusicPlayer.music_play()
    second_ord.show("agronom", "agronom_normal", bsc_tuple[0], bsc_tuple[1])
    second_ord.tell('agronom', 'А вот и он, долгожданный грузчик, почему вы так долго?')
    second_ord.tell('i', 'Извините, по всему городу пробки, я пытался ехать быстрее')
    second_ord.tell('agronom', 'Пф... ЭТО всего лишь оправдания вашей безответственности')
    second_ord.tell('agronom', 'Ну ладно, товар лежит у забора, иди же наконец и выполняй свою работу')
    second_ord.tell("i", 'Хорошо, можно узнать что конкретно мне предстоит перевезти?')
    second_ord.tell('agronom', 'Тебя это волновать не должно, просто погрузи те коробки и проваливай')
    second_ord.tell("i", 'Ладно, простите за излишнее любопытство')
    second_ord.tell('agronom', '...')
    second_ord.bg_img()
    second_ord.hide()
    MusicPlayer.music_stop()
    second_ord.tell('na', '~ я опоздал всего на 2 минуты, почему она так разозлилась ~')


def start_second_order():
    second_order_start_init()
    second_order_start()
    pygame.display.flip()

if(__name__ == "__main__"):
    start_second_order()
