'''
class containing the healthbars for left character
'''


import pygame
from HelperFunctions import *

class Hp_Bar_Left(pygame.sprite.Sprite):
    """generates a health bar"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('Hb1.png', 'HealthBar')
        self.image.set_colorkey((255,255,255))

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

    def update(self):

        return None




class Hp_Bar_Right(pygame.sprite.Sprite):
    """generates a health bar"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('Hb1.png', 'HealthBar')
        self.image.set_colorkey((255,255,255))
        self.image = pygame.transform.flip(self.image, 1, 0)

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

    def update(self):

        return None