
'''
Background sprite
'''

import pygame
from HelperFunctions import *




class Background(pygame.sprite.Sprite):
    '''generates the background and contains logic to make it scroll'''

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image("b5.jpg", 'Backgrounds')

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.Current_Animation = 'Idle'

        self.Map_Movement_Factor = 12

    def update(self):

        if self.Current_Animation=='Idle':
            '''do nothing'''
            return None

        elif self.Current_Animation=='Move_Left':

            self.image, self.rect = load_image("b5.jpg", 'Backgrounds')

            self.Current_X_position+=-self.Map_Movement_Factor
            
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

        elif self.Current_Animation=='Move_Right':

            self.image, self.rect = load_image("b5.jpg", 'Backgrounds')

            self.Current_X_position+=self.Map_Movement_Factor
            
            self.rect.topleft = self.Current_X_position, self.Current_Y_position


    def Update_Animation(self, anim):
        '''this function can ba called from outide to change the current animation sequence'''

        self.Current_Animation = anim




class Collision_Line(pygame.sprite.Sprite):

    def __init__(self, Start_X, Start_Y, width, height):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image = pygame.Surface([width,height])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.y = Start_Y
        self.rect.x = Start_X



class HenesysTiles(pygame.sprite.Sprite):
    '''generates the tiles for henesys'''

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_skill_image('enH0_2.png', 'MapData', 'Henesys')

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.Current_Animation = 'Idle'

    def Update(self):

        return None
