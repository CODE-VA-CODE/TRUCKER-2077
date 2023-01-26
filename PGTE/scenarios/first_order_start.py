import pygame

from MakeButton import MusicPlayer
from PGTE.pgte_engine import scenario_commands


def first_order_start_init():
    global first_ord
    first_ord = scenario_commands()
    first_ord_sprites = {'worker_norm': 'data/images/sprites/first_order/worker_norm.png',
                         'worker_shock': 'data/images/sprites/first_order/worker_shock.png',
                         'worker_question': 'data/images/sprites/first_order/worker_question.png',
                         'worker_answer': 'data/images/sprites/first_order/worker_answer.png'}
    first_ord.pers_init("Поставщик", (215, 215, 215), "worker", first_ord_sprites)
    first_ord.init_music("data/music/Shiro Sagisu - Cruel Dilemme III", "farmer_music")
    first_ord.pers_init("Я", (215, 215, 215), "i", {"none":"none"})
    first_ord.pers_init("", (213, 213, 213), "na", {"none":"none"}) # рассказчик/просто описание происходящего
    first_ord.init_bg("data/images/bg/sklad.png", "sklad_bg")

def first_order_start():
    global first_ord
    bsc_tuple = (450, 250)
    first_ord.tell("i", "Фух, вроде добрался")
    first_ord.bg_img("sklad_bg")
    MusicPlayer.music_load('data/music/quitemusic.mp3')
    MusicPlayer.music_play()
    first_ord.show("worker", "worker_norm", bsc_tuple[0], bsc_tuple[1])
    first_ord.tell('worker', 'Так, здравствуйте, вы верно привезли мне еду из ресторана?')
    first_ord.tell('na', '~ он вообще о чём ~')
    first_ord.tell("i", "Нет, я дальнобойщик, приехал за товаром")
    first_ord.show("worker", "worker_shock", bsc_tuple[0], bsc_tuple[1])
    first_ord.tell('worker', 'A, ой, извините...')
    first_ord.show("worker", "worker_question", bsc_tuple[0], bsc_tuple[1])
    first_ord.tell('worker', 'Так за какой вы посылкой говорите приехали?')
    first_ord.tell('na', '~ мда... очень ответственный сотрудник ~')
    first_ord.tell("i", "За строительными материалами для стройки на юге города")
    first_ord.show("worker", "worker_answer", bsc_tuple[0], bsc_tuple[1])
    first_ord.tell('worker', 'Ах да, точно, вспомнил!')
    first_ord.show("worker", "worker_norm", bsc_tuple[0], bsc_tuple[1])
    first_ord.tell('worker', 'Можешь забрать материалы в конце склада, постарайся доставить их в целости и сохранности')
    first_ord.tell("i", "Да хорошо, сейчас приступлю")
    first_ord.bg_img()
    first_ord.hide()
    MusicPlayer.music_stop()
    first_ord.tell('na', '"""Вы уходите и начинаете погрузку материалов"""')
    first_ord.tell('na', '~ Надо будет обязательно рассказать боссу про этого дурачка ~')


def start_first_order():
    first_order_start_init()
    first_order_start()
    pygame.display.flip()

if(__name__ == "__main__"):
    start_first_order()
