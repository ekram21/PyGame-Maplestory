
import pygame
from HelperFunctions import *




class Time_Countdown_Right(pygame.sprite.Sprite):
    '''generats the left digit of time which will change every second'''

    def __init__(self, Start_X, Start_Y, Game_fps):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('0.png', 'Time')
        self.image.set_colorkey((0,0,0))

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.count = 0

        self.Time_Checking_List = []
        self.Time_Scaler = Game_fps

    def update(self):

        self.Time_Checking_List.append(self.count)

        FileName = str(self.count) + '.png'
        self.image, self.rect = load_image(FileName, 'Time')
        self.image.set_colorkey((0,0,0))

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        if len(self.Time_Checking_List)==self.Time_Scaler:
            self.count+=1
            self.Time_Checking_List = []
        else:
            self.count+=0

        if self.count==11:
            self.count=1

        return None


class Time_Countdown_Left(pygame.sprite.Sprite):
    '''generats the right digit of time which will change every 10 second'''

    def __init__(self, Start_X, Start_Y, Game_fps):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('0.png', 'Time')
        self.image.set_colorkey((0,0,0))

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.count = 0

        self.Time_Checking_List = []
        self.Time_Scaler = Game_fps*10

    def update(self):

        self.Time_Checking_List.append(self.count)

        FileName = str(self.count) + '.png'
        self.image, self.rect = load_image(FileName, 'Time')
        self.image.set_colorkey((0,0,0))

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        if len(self.Time_Checking_List)==self.Time_Scaler:
            self.count+=1
            self.Time_Checking_List = []
        else:
            self.count+=0

        if self.count==11:
            self.count=1


