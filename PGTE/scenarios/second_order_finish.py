import pygame

from MakeButton import MusicPlayer
from PGTE.pgte_engine import scenario_commands


def second_order_finish_init():
    global second_ord_fin
    second_ord_fin = scenario_commands()
    second_ord_sprites = {'shopper_normal': 'data/images/sprites/second_order/shopper_normal.png',
                          'shopper_happy': 'data/images/sprites/second_order/shopper_happy.png'}
    second_ord_fin.pers_init("Продавец", (215, 215, 215), "shopper", second_ord_sprites)
    second_ord_fin.init_music("data/music/Shiro Sagisu - Cruel Dilemme III", "farmer_music")
    second_ord_fin.pers_init("Я", (215, 215, 215), "i", {"none":"none"})
    second_ord_fin.pers_init("", (213, 213, 213), "na", {"none":"none"}) # рассказчик/просто описание происходящего
    second_ord_fin.init_bg("data/images/bg/shop.png", "shop_bg")


def second_order_finish():
    bsc_tuple = (450, 270)
    second_ord_fin.tell("i", "Видимо это и есть тот самый магазин")
    second_ord_fin.bg_img("shop_bg")
    MusicPlayer.music_load('data/music/quitemusic.mp3')
    second_ord_fin.show("shopper", "shopper_normal", bsc_tuple[0], bsc_tuple[1])
    MusicPlayer.music_play()
    second_ord_fin.tell("shopper", "Ппривет... Ты привёз товар для магазина?")
    second_ord_fin.tell('na', '~ похоже ему совсем не занимать увереностью в себе ~')
    second_ord_fin.tell("i", "Да, всё верно, товар в грузовике, можете его забрать")
    second_ord_fin.tell("shopper", "Ххорошо, ссейчас")
    second_ord_fin.bg_img()
    second_ord_fin.hide()
    second_ord_fin.tell('na', '~ вы помогаете бедолаге разгрузить грузовик ~')
    second_ord_fin.bg_img("shop_bg")
    second_ord_fin.show("shopper", "shopper_normal", bsc_tuple[0], bsc_tuple[1])
    second_ord_fin.tell("shopper", "Спасибо за ппомощь")
    second_ord_fin.tell("i", "Всё в порядке, это моя работа")
    second_ord_fin.tell("shopper", "И ещё одно маленькое уточнение...")
    second_ord_fin.tell("i", "?")
    second_ord_fin.tell("shopper", "Вы ведь знаете что лежит в этих коробках?")
    second_ord_fin.tell("i", "Нет, я хотел узнать, но ваш поставщик сказал что это не моё дело")
    second_ord_fin.show("shopper", "shopper_happy", bsc_tuple[0], bsc_tuple[1])
    second_ord_fin.tell("shopper", "ННу, в целом она пправа")
    second_ord_fin.tell("i", "...")
    second_ord_fin.show("shopper", "shopper_normal", bsc_tuple[0], bsc_tuple[1])
    second_ord_fin.tell("shopper", "Вот ваши деньги, вы мможете быть ссвободны")
    second_ord_fin.bg_img()
    second_ord_fin.hide()
    MusicPlayer.music_stop()
    second_ord_fin.tell('na', '~ вы молча берёте деньги и направляетесь к боссу за ответами ~')


def finish_second_order():
    second_order_finish_init()
    second_order_finish()
    pygame.display.flip()

if(__name__ == "__main__"):
    finish_second_order()
