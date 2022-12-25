import os
import sys
import pygame


pygame.init()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
FPS = 60
clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class MakeButton(pygame.sprite.Sprite):
    def __init__(self, *group, first_style, first_style_background=None, pos, size=None,
                 second_style=None, second_style_background=None, if_chage_style=False, when_see=True):
        #переменные first_style и first_style_background отвечают за инициализацию базовой картинки
        #переменные pos и size отвечают за позицию и размер кнопки соответственно
        #переменные second_style, second_style_background и if_chage_style являются необязательными отвечают за смену
        #дизайна кнопки при наведении мышкой наведении на неё курсора мыши
        #переменная when_see отвечает за условие при котором кнопка будет видна
        super().__init__(*group)
        self.first_style = load_image(first_style, first_style_background)
        if second_style != None:
            self.second_style = load_image(second_style, second_style_background)
        if size != None:
            self.first_style = pygame.transform.scale(self.first_style, size)
        self.button_rect = self.first_style.get_rect()
        self.copy_of_first_style = self.first_style
        self.button_rect.x, self.button_rect.y = pos
        self.pos = pos
        self.when_see = when_see
        self.if_chage_style = if_chage_style

    def update(self, *args):
        if self.when_see:
            screen.blit(self.first_style, self.pos)
        if self.if_chage_style and self.button_rect.collidepoint(args[0].pos):
            self.first_style = self.second_style
        if self.if_chage_style and self.button_rect.collidepoint(args[0].pos) == False:
            self.first_style = self.copy_of_first_style
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.button_rect.collidepoint(args[0].pos):
            pass



class MainMenu(pygame.sprite.Sprite):
        main_image = load_image("MainMenu\MainMenu.png")

        def __init__(self, *group):
            super().__init__(*group)
            self.main_image = MainMenu.main_image
            self.rect = self.main_image.get_rect()
            self.rect.x, self.rect.y = 0, 0

        def update(self, *args):
            screen.blit(self.main_image, (0, 0))
            #key = pygame.key.get_pressed()
            #if key[pygame.K_LEFT]:
                #self.rect.x -= 10
            #if key[pygame.K_RIGHT]:
                #self.rect.x += 10
            #if key[pygame.K_UP]:
                #self.rect.y -= 10
            #if key[pygame.K_DOWN]:
                #self.rect.y += 10


while True:
    MainMenuButtonGroup = pygame.sprite.Group()
    Mainmenu = MainMenu()
    ContinueButton = MakeButton(first_style="MainMenu\ContinueButton.png", first_style_background=-1, pos=[0, 0],
                                size=(100, 100))
    MainMenuButtonGroup.add(Mainmenu, ContinueButton)
    MainMenuButtonGroup.update()
    for event in pygame.event.get():
        MainMenuButtonGroup.update(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(FPS)