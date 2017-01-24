'''
class containing the demon power up for characters
'''


import pygame
from HelperFunctions import *

class Demon_Power_Up(pygame.sprite.Sprite):
    """generates a swirling demon power up around character"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('40.gif', 'DemonPowerUp')
        self.image.set_colorkey((255,255,255))

        self.Base_X_Position = Start_X
        self.Base_Y_Position = Start_Y

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.count = 1

        self.Current_Animation = 'Show'

        self.Show_Bool = False #If true will show the skill/if false will not show it
        self.Facing_Side='Left'

    def update(self):

        if self.Current_Animation=='Show':

            if self.Show_Bool:
                self.Current_X_position = self.Base_X_Position
                self.Current_Y_position = self.Base_Y_Position

                FileName = str(self.count) + '.gif'
                self.image, self.rect = load_image(FileName, 'DemonPowerUp')
                self.image.set_colorkey((255,255,255))

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()

                if self.count>21 and self.count<34:
                    '''frames over 21.gif are slightly offset so this section is to fix that'''
                    self.Current_X_position+=-5
                    self.Current_Y_position+=7
                elif self.count>33 and self.count<41:
                    self.Current_X_position+=-5
                    self.Current_Y_position+=-15

                #fixing vertical offset
                self.Current_Y_position+=87

                #fixing x offset
                if self.Facing_Side=='Left':
                    self.Current_X_position+=10
                elif self.Facing_Side=='Right':
                    self.Current_X_position+=-28

                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.count+=1

                if self.count==41:
                    self.Show_Bool=False

            else:
                self.count = 1
                return None

    def Show_Animation(self):
        '''when called will flip the animation boolean to show'''
        self.Show_Bool=True

    def Update_Current_positions(self, x, y):
        '''called from outside to set the current x and y poisiton of the animation'''

        self.Base_X_Position = x
        self.Base_Y_Position = y

    def Update_Side_Facing(self, word):
        '''updates which side the character is facing'''

        if word=='Left':
            self.Facing_Side='Left'
        elif word=='Right':
            self.Facing_Side='Right'



