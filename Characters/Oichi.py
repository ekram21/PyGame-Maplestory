'''
Oichi animation and sprites. Root class
'''

import pygame
from HelperFunctions import *

class Oichi(pygame.sprite.Sprite):
    '''
    Oichi class sprite
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.Background_Whitespace = (0,248,0)

        self.image, self.rect = load_image('1.png', 'OichiIdle')
        self.image.set_colorkey(self.Background_Whitespace)

        self.Base_X_Poistion = 200
        self.Base_Y_position = 626

        self.Current_X_position = 200
        self.Current_Y_position = 626

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.Current_Animation = 'Idle'

        self.Facing_Side = 'Left'

        self.count = 2

        self.Checking_List_Idle = []
        self.Idle_Scaler = 3

        self.Checking_List_Walk = []
        self.Walk_Scaler = 3

        self.Checking_List_JumpStr8Up = []
        self.JumpStraightUp_Scaler = 2

        self.Reverse_Frames = False #this boolean if true will make the frames animate in reverse, while in false mode it will make the frames go forward

    def update(self):
        

        if self.Current_Animation=='Idle':
            '''call the frames of idle animation one after another here'''

            self.Checking_List_Idle.append(self.count)

            FileName = str(self.count) + '.png'
            self.image, self.rect = load_image(FileName, 'OichiIdle')

            if self.Facing_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)

            self.image.set_colorkey(self.Background_Whitespace)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()

            self.Current_Y_position = self.Base_Y_position

            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            if self.Reverse_Frames==False:
                '''propagate the frames incrementally forward'''
                if len(self.Checking_List_Idle)==self.Idle_Scaler:
                    self.count+=1
                    self.Checking_List_Idle = []
                else:
                    self.count+=0

                if self.count==14:
                    self.Reverse_Frames = True
                    self.count=13

            elif self.Reverse_Frames==True:
                '''reverse the frames to 0 again at which point it will animate forwards again'''
                if len(self.Checking_List_Idle)==self.Idle_Scaler:
                    self.count+=-1
                    self.Checking_List_Idle = []
                else:
                    self.count+=0

                if self.count==0:
                    self.Reverse_Frames = False
                    self.count=1

        elif self.Current_Animation=='Walk':

            self.Checking_List_Walk.append(self.count)

            FileName = str(self.count) + '.png'
            self.image, self.rect = load_image(FileName, 'OichiWalk')

            if self.Facing_Side=='Left':
                self.Current_X_position+=16
            elif self.Facing_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)
                self.Current_X_position+=-16

            self.image.set_colorkey(self.Background_Whitespace)
            self.Current_Y_position = self.Base_Y_position
            self.Current_Y_position+=-58

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_Walk)==self.Walk_Scaler:
                self.count+=1
                self.Checking_List_Walk = []
            else:
                self.count+=0

            if self.count==11:
                self.count=1

        elif self.Current_Animation=='JumpStraightUp':

            self.Checking_List_JumpStr8Up.append(self.count)

            FileName = str(self.count) + '.png'
            self.image, self.rect = load_image(FileName, 'OichiJump')

            if self.count<6 and self.count>0:
                '''animate going up'''
                self.Current_Y_position+=-15
            elif self.count>5 and self.count<12:
                '''animate coming down'''
                self.Current_Y_position+=10
            elif self.count>12:
                '''animate landing'''
                self.Current_Y_position=self.Base_Y_position+20

            if self.Facing_Side=='Left':
                if self.count<13:
                    '''13th frame afterwards needs a offset'''
                    self.Current_X_position+=9
                else:
                    self.Current_X_position+=-4
            else:
                self.image = pygame.transform.flip(self.image, 1, 0)
                if self.count<13:
                    '''13th frame afterwards needs a offset'''
                    self.Current_X_position+=-9
                else:
                    self.Current_X_position+=2

            self.image.set_colorkey(self.Background_Whitespace)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_JumpStr8Up)==self.JumpStraightUp_Scaler:
                self.count+=1
                self.Checking_List_JumpStr8Up = []
            else:
                self.count+=0

            if self.count==17:
                self.count=1
                self.Current_Animation='Idle'
   
    def Update_Animation(self, anim):
        '''this function can be called from outide to change the current animation sequence'''

        self.count = 1
        self.Current_Animation = anim

    def Update_Facing_Side(self, direction):
        '''will update which side the character is currently facing now'''
        self.Facing_Side = direction

    def Change_Current_X_Position(self, value):
        '''changes the current x position'''
        self.Current_X_position+=value 
        self.Base_X_Poistion = self.Current_X_position




class OichiPotrait(pygame.sprite.Sprite):
    """generates a health bar"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('OichiPotrait.png', 'Oichi')
        self.image.set_colorkey((255,255,255))

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

    def update(self):

        return None

class OichiLogo(pygame.sprite.Sprite):
    """generates a logo text of Oichi"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('OichiLogo.png', 'Oichi')
        self.image.set_colorkey((0,0,0))

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

    def update(self):

        return None