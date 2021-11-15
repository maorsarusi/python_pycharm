import pygame

BASEBALL = r"C:\Network\work\shapes\Baseball.jpg"
COLOR = (255, 255, 255)
HORIZONTAL = 5
VERTICAL = 5


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Ball, self).__init__()
        self.image = pygame.image.load(BASEBALL)
        self.image.set_colorkey(COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = HORIZONTAL
        self.__vy = VERTICAL

    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_location(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy
