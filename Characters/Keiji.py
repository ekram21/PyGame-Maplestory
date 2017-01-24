'''
Keiji animation and sprites. Root class
'''

import pygame
from HelperFunctions import *

class Keiji(pygame.sprite.Sprite):
    '''
    Keiji class sprite
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('1idlen.png', 'Keiji Maeda')
        self.image.set_colorkey((255,0,250))

        self.Current_X_position = 200
        self.Current_Y_position = 585
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.Current_Animation = 'Idle'

        self.count = 2

        self.Checking_List_Idle = []
        self.Idle_Scaler = 5

    def update(self):
        '''call the frames of idle animation one after another here'''

        if self.Current_Animation=='Idle':

            self.Checking_List_Idle.append(self.count)

            FileName = str(self.count) + 'idlen.png'
            self.image, self.rect = load_image(FileName, 'Keiji Maeda')
            self.image.set_colorkey((255,0,250))

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_Idle)==self.Idle_Scaler:
                self.count+=1
                self.Checking_List_Idle = []
            else:
                self.count+=0

            if self.count==23:
                self.count=1

        elif self.Current_Animation=='Walk_Right':

            FileName = str(self.count) + 'walk.png'
            self.image, self.rect = load_image(FileName, 'Keiji Maeda')
            self.image.set_colorkey((255,0,250))

            self.Current_X_position+=5

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1


            if self.count==21:
                self.count=1
   
    def Update_Animation(self, anim):
        '''this function can ba called from outide to change the current animation sequence'''

        self.count = 1
        self.Current_Animation = anim