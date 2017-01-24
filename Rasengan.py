'''
class containing the rasengan attack for characters
'''


import pygame
from HelperFunctions import *

class Rasengan(pygame.sprite.Sprite):
    """generates a swirling rasengan attack in front of chracter"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('8.png', 'FlyingRasengan')
        self.image.set_colorkey((0,255,0))

        self.Base_X_Position = Start_X
        self.Base_Y_Position = Start_Y

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.count = 1

        self.Current_Animation = 'Show_Static'

        self.Show_Bool = False #If true will show the skill/if false will not show it
        self.Facing_Side='Left'

        self.Checking_List = [] #everytime the image is read this will be filled up with it ,needed for independant fps scaler of animations
        self.Static_Rasengan_Scaler = 1

        self.Set_Static_Rasengan_Scaler(2)

    def update(self):

        if self.Current_Animation=='Show_Static':

            if self.Show_Bool:
                self.Current_X_position = self.Base_X_Position
                self.Current_Y_position = self.Base_Y_Position

                self.Checking_List.append(self.count)

                FileName = str(self.count) + '.png'
                self.image, self.rect = load_image(FileName, 'FlyingRasengan')
                self.image.set_colorkey((0,255,0))

                self.Current_Y_position+=-35

                if self.Facing_Side=='Left':
                    self.image = pygame.transform.flip(self.image, 1, 0)
                    self.Current_X_position+=-40
                else:
                    self.Current_X_position+=110

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()

                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                if len(self.Checking_List)==self.Static_Rasengan_Scaler:
                    '''this section is to check with the independant fps scaler of this animation and how many 
                    times to repeat each image'''
                    self.count+=1
                    self.Checking_List=[]
                else:
                    self.count+=0

                if self.count==8:
                    '''restarting animation from start again'''
                    self.count=1

            else:
                '''Hide the animation'''
                self.count = 1
                self.image, self.rect = load_image('8.png', 'FlyingRasengan')
                self.image.set_colorkey((0,255,0))
                self.rect.topleft = self.Current_X_position, self.Current_Y_position


    def Show_Animation(self):
        '''when called will flip the animation boolean to show'''
        self.Show_Bool=True

    def Hide_Animation(self):
        '''when called will hide the animation'''

        self.Show_Bool=False

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

    def Sprite_Fps_Scaler(self, scaler):
        '''this will accept a scaler and return true if each image has been repeated enough times'''

        if len(self.Checking_List)==scaler:
            return True
        else:
            return False

    def Set_Static_Rasengan_Scaler(self, scaler):
        '''this will set the scaler'''

        self.Static_Rasengan_Scaler = scaler



