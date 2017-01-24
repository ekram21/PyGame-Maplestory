
'''
class containing the mouse pointer for pygame
'''


import pygame
from HelperFunctions import *

class Hand(pygame.sprite.Sprite):
    """moves a hand on the screen, following the mouse"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('Hand.png', 'Mouse')
        self.image.set_colorkey((255,242,0))
        self.punching = 0

    def update(self):
        "move the fist based on the mouse position"
        self.pos = pygame.mouse.get_pos()
        #print (self.pos)
        self.rect.midtop = self.pos

    def Get_Current_Mouse_POS(self):

        return self.pos