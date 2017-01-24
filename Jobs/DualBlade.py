'''
Dual blade job skills
'''

import pygame
from HelperFunctions import *




class BladeFury(pygame.sprite.Sprite):
    '''generates the blade fury skill for dual blades'''

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_skill_image('effect_0.png', 'DualBlade', 'BladeFury')
        self.image.set_colorkey((0,0,0))

        '''starting offsets'''
        self.Current_X_position = Start_X - 190
        self.Current_Y_position = Start_Y - 100

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.count = 0

        self.Skill_Checking_List = []
        self.Skill_Scaler = 2

    def update(self):

        self.Skill_Checking_List.append(self.count)

        FileName =  'effect_' + str(self.count) + '.png'
        self.image, self.rect = load_skill_image(FileName, 'DualBlade', 'BladeFury')
        self.image.set_colorkey((0,0,0))

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        if len(self.Skill_Checking_List)==self.Skill_Scaler:
            self.count+=1
            self.Skill_Checking_List = []
        else:
            self.count+=0

        if self.count==8:
            self.count=0

        return None

class PhantomBlow(pygame.sprite.Sprite):
    '''generates the phantom blow skill for dual blades'''

    def __init__(self, Start_X, Start_Y, side):

        self.Current_Faced_Side = side

        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_skill_image('effect_0.png', 'DualBlade', 'PhantomBlow')

        if self.Current_Faced_Side=='Right':
            self.image = pygame.transform.flip(self.image, 1, 0)

        self.image.set_colorkey((0,0,0))

        '''starting offsets'''
        self.Current_X_position = Start_X - 120
        self.Current_Y_position = Start_Y - 70

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.count = 0

        self.Skill_Checking_List = []
        self.Skill_Scaler = 1

    def update(self):

        self.Skill_Checking_List.append(self.count)

        FileName =  'effect_' + str(self.count) + '.png'
        self.image, self.rect = load_skill_image(FileName, 'DualBlade', 'PhantomBlow')

        if self.Current_Faced_Side=='Right':
            self.image = pygame.transform.flip(self.image, 1, 0)

        self.image.set_colorkey((0,0,0))

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        if len(self.Skill_Checking_List)==self.Skill_Scaler:
            self.count+=1
            self.Skill_Checking_List = []
        else:
            self.count+=0

        if self.count==10:
            self.count=0

        return None