import pygame


file = 'data/music/vespercellos_all_go_to_plan.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
pygame.quit()