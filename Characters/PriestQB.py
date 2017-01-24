'''
priest animations from the queensblade sprites
'''

import pygame
from HelperFunctions import *

class Priest(pygame.sprite.Sprite):
    '''
    the priest fighting girl
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('1idle.png', 'PriestQB')

        self.Current_X_position = 100
        self.Current_Y_position = 580
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.Current_Animation = 'Idle'
        self.Upper_Attack_Bool = False #this gives true to see if the previous animation seq was upper attack
        self.Taunt_Bool = False
        self.move = 2

        self.count = 2

    def update(self):
        '''call the frames of idle animation one after another here'''

        if self.Upper_Attack_Bool==True:
            '''Correcting the offset which was imposed when in the previous animation seq upper attack
                was carried out
            '''
            self.Current_X_position+=-24
            self.Current_Y_position+=12

        if self.Taunt_Bool==True:
            '''Correcting the offset which was imposed when in the previous animation seq taunt
                was carried out
            '''
            self.Current_X_position+=-28
        
        if self.Current_Animation=='Idle':
            FileName = str(self.count) + 'idle.png'
            self.image, self.rect = load_image(FileName, 'PriestQB')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Upper_Attack_Bool=False
            self.Taunt_Bool = False

            if self.count==7:
                self.count=1

        elif self.Current_Animation=='Walk_Right':

            self.Current_X_position+=20
            FileName = str(self.count) + 'walk.png'
            self.image, self.rect = load_image(FileName, 'PriestQB')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()

            print (self.Current_X_position)
            print (self.area.right)

            if self.Current_X_position<1650:
                self.rect = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position = 1650
                self.rect = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Upper_Attack_Bool=False
            self.Taunt_Bool = False

            if self.count==7:
                self.count=1

        elif self.Current_Animation=='Walk_Left':

            self.Current_X_position+=-20
            FileName = str(self.count) + 'walk.png'
            self.image, self.rect = load_image(FileName, 'PriestQB')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()

            print (self.Current_X_position)
            print (self.area.right)

            if self.Current_X_position>0:
                self.rect = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position = 0
                self.rect = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Upper_Attack_Bool=False
            self.Taunt_Bool = False

            if self.count==7:
                self.count=1

        elif self.Current_Animation=='Taunt1':

            self.Current_X_position+=28
            FileName = str(self.count) + 'taunt1.png'
            self.image, self.rect = load_image(FileName, 'PriestQB')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Upper_Attack_Bool=False
            self.Taunt_Bool = True

            if self.count==5:
                self.count=1

        elif self.Current_Animation=='Taunt2':

            self.Current_X_position+=28
            FileName = str(self.count) + 'taunt2.png'
            self.image, self.rect = load_image(FileName, 'PriestQB')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Upper_Attack_Bool=False
            self.Taunt_Bool = True

            if self.count==5:
                self.count=1

        elif self.Current_Animation=='Taunt3':

            self.Current_X_position+=28
            FileName = str(self.count) + 'taunt3.png'
            self.image, self.rect = load_image(FileName, 'PriestQB')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Upper_Attack_Bool=False
            self.Taunt_Bool = True

            if self.count==5:
                self.count=1

        elif self.Current_Animation=='Upper_Attack':
            '''this animation is a bit offcenter so must be offset by shifting a bit to the topright. Figure it out later'''

            self.Current_X_position+=24
            self.Current_Y_position+=-12

            FileName = str(self.count) + 'attack1.png'
            self.image, self.rect = load_image(FileName, 'PriestQB')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Upper_Attack_Bool=True
            self.Taunt_Bool = False

            if self.count==6:
                self.count=1

    def Update_Animation(self, anim):
        '''this function can ba called from outide to change the current animation sequence'''

        self.count = 1
        self.Current_Animation = anim